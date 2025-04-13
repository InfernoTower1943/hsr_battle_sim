from equippables import *

class Entity:
    name: str = "Entity"
    base_hp: float = -1
    base_atk: float = -1
    base_def: float = -1
    base_spd: float = -1
    ehr: float = -1
    effres: float = -1
    ccres: float = -1
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
    critrate: float = 5
    critdmg: float = 50
    path: str = None

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.stats = stats

class Character(Ally):
    name = "The Herta"
    real_base_hp: float = base_hp
    real_base_atk: float = base_atk
    real_base_def: float = base_def
    # TODO: implement traces
    max_energy: float = 160
    current_energy: float = 0
    lightcone: Lightcone = None

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.stats = stats
    
    def setLightcone(self, lightcone):
        self.lightcone = lightcone
        self.real_base_hp = self.base_hp + lightcone.base_hp
        self.real_base_atk = self.base_atk + lightcone.base_atk
        self.real_base_def = self.base_def + lightcone.base_def
        
        # Add lightcone's abilities only if paths match
        if self.lightcone.path == self.path:
            pass

class Summon(Ally):
    name = "Summon"
    master: Character = "Character"
    is_memosprite: bool = False

    def __init__(self, name, stats):
        super().__init__(name, stats)
        self.stats = stats