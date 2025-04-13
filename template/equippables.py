class Relic:
    set = ""
    abilities = []
    mainstat = []
    substats = {}
    def __init__(self, stats):
        self.stats = stats

    def __repr__(self):
        return f"Relic(name={self.name}, description={self.description}, rarity={self.rarity}, stats={self.stats})"
    
    # TODO: set substats
    # TODO: roll value 

class CavernRelic(Relic):
    name = "Eagle"
    two_piece_ability = []
    four_piece_ability = []
    TYPE_HEAD = 0
    TYPE_GLOVE = 1
    TYPE_BODY = 2
    TYPE_BOOT = 3
    # TODO: set the type of relic
    # TODO: lock mainstats behind relic type

class PlanarOrnament(Relic):
    name = "Izumo"
    two_piece_ability = []
    TYPE_ORB = 0
    TYPE_ROPE = 1
    # TODO: set the type of relic
    # TODO: lock mainstats behind relic type
    
class Lightcone:
    name = "Passkey"
    path = None
    base_hp: float = 1000
    base_atk: float = 100
    base_def: float = 50
    abilities = []
    def __init__(self, name, description, rarity, stats):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.stats = stats

    def __repr__(self):
        return f"Lightcone(name={self.name}, description={self.description}, rarity={self.rarity}, stats={self.stats})"