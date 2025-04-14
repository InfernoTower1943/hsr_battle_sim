from enum import Enum
class Element(Enum):
    PHYSICAL = 1
    FIRE = 2
    ICE = 3
    LIGHTNING = 4
    WIND = 5
    QUANTUM = 6
    IMAGINARY = 7

def damage_formula_crit():
    """
    DMG =  Base DMG(Attacker) x CRIT Multiplier(Attacker) x DMG Boost(Attacker) x Weaken Multiplier(Attacker)
            x DEF Multiplier(Target) x RES Multiplier(Target) x Vuln(Target) x DMG Reduction(Target) x Broken Multiplier(Target)
    """
    return 0

def damage_formula_break():
    return 0

def damage_formula_superbreak():
    return 0

def damage_formula_dot():
    return 0