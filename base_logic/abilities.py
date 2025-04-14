class Ability:
    def __init__(self, name, energy_generation, energy_cost, damage_multipliers=[100], description="No Description"):
        self.name = name
        self.description = description
        self.energy_generation = energy_generation
        self.energy_cost = energy_cost
        self.damage_multipliers = damage_multipliers
        self.toughness = None # TODO: implement toughness damage
        self.tag = None # TODO: implement tags (e.g. Single Target, AoE, etc.)

    def __repr__(self):
        return f"Ability(name={self.name}, energy_generation={self.energy_generation}, energy_cost={self.energy_cost}, damage_multipliers={self.damage_multipliers}, description={self.description})"
    
class BasicAttack(Ability):
    def __init__(self, name, energy_generation=20, energy_cost=0, damage_multipliers=[100], description="No Description"):
        super().__init__(name, energy_generation, energy_cost, damage_multipliers, description)
        self.is_basic_attack = True
        self.is_ultimate = False
        self.is_skill = False
        self.is_talent = False
        self.is_passive = False

class Skill(Ability):
    def __init__(self, name, energy_generation=30, energy_cost=0, damage_multipliers=[100], description="No Description"):
        super().__init__(name, energy_generation, energy_cost, damage_multipliers, description)
        self.is_basic_attack = False
        self.is_ultimate = False
        self.is_skill = True
        self.is_talent = False
        self.is_passive = False

class Ultimate(Ability):
    def __init__(self, name, energy_generation=5, energy_cost=160, damage_multipliers=[100], description="No Description"):
        super().__init__(name, energy_generation, energy_cost, damage_multipliers, description)
        self.is_basic_attack = False
        self.is_ultimate = True
        self.is_skill = False
        self.is_talent = False
        self.is_passive = False

class Talent(Ability):
    def __init__(self, name, energy_generation=0, energy_cost=0, damage_multipliers=[100], description="No Description"):
        super().__init__(name, energy_generation, energy_cost, damage_multipliers, description)
        self.is_basic_attack = False
        self.is_ultimate = False
        self.is_skill = False
        self.is_talent = True
        self.is_passive = False

class Passive(Ability):
    def __init__(self, name, energy_generation, energy_cost, damage_multipliers=[100], description="No Description"):
        super().__init__(name, energy_generation, energy_cost, damage_multipliers, description)
        self.is_basic_attack = False
        self.is_ultimate = False
        self.is_skill = False
        self.is_talent = False
        self.is_passive = True

class AscensionTrace(Ability):
    # TODO: Implement ascension traces
    pass

class Eidolon(Ability):
    # TODO: Implement eids
    pass