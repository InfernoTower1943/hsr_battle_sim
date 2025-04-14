from equippables import *
import base_logic.math.damage as damage

class Entity:
    name: str = "Entity"
    base_stats: dict = {
        "hp": 0,
        "atk": 0,
        "def": 0,
        "spd": 0,
        "ehr": 0,
        "effres": 0,
        "ccres": 0
    }
    buffs: float = []
    debuffs: float = []
    abilities = []

    def __init__(self, name, stats):
        self.name = name
        # TODO: fill out the stats
        # self.stats = stats
        self.stats = stats

    def __repr__(self):
        return f"Entity({self.name}, {self.stats})"
    
class Enemy(Entity):
    is_boss = False
    max_toughness = 0
    current_toughness = 0
    weaknesses = []
    resistances = []
    in_state = False
    attacks = []
    
class Ally(Entity):
    name: str = "Allied Entity"
    crit_rate: float = 0.05
    crit_dmg: float = 0.50
    path: str = None
    element: damage.Element = None

    def __init__(self, name, stats, crit_rate=0.05, crit_dmg=0.50, path=None):
        super().__init__(name, stats)
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg
        self.path = path

class Character(Ally):
    name = "Character"
    # TODO: implement traces
    max_energy: float = 160
    current_energy: float = 0
    lightcone: Lightcone = None

    def __init__(self, name, stats, crit_rate=0.05, crit_dmg=0.50):
        super().__init__(name, stats, crit_rate, crit_dmg)
        self.base_hp = self.stats.get("hp", -1)
        self.base_atk = self.stats.get("atk", -1)
        self.base_def = self.stats.get("def", -1)

        # Real base stats (including lightcone)
        self.stats_screen_base_hp = self.base_hp
        self.stats_screen_base_atk = self.base_atk
        self.stats_screen_base_def = self.base_def

        # Ability slots - can assign functions later
        self.basic_attack = None
        self.skill = None
        self.ultimate = None
        self.talent = None
        self.memosprite_skill = None
        self.memosprite_talent = None
        self.ascension2 = None
        self.ascension4 = None
        self.ascension6 = None
        self.eidolons = [None, None, None, None, None, None]
        self.stat_traces = {}
    
    def setLightcone(self, lightcone):
        self.lightcone = lightcone
        self.stats_screen_base_hp = self.base_hp + lightcone.base_hp
        self.stats_screen_base_atk = self.base_atk + lightcone.base_atk
        self.stats_screen_base_def = self.base_def + lightcone.base_def
        
        # Add lightcone's abilities only if paths match
        if self.lightcone.path == self.path:
            self.lightcone.enabled = True
        else:
            self.lightcone.enabled = False

class Summon(Ally):
    name = "Summon"
    master: Character = "Character"
    is_memosprite: bool = False

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.stats = stats
        # TODO: implement this. get to it only when doing topaz and castorice