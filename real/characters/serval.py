from base_logic import entities
from base_logic.math import damage

SERVAL = entities.Character(
    name="Serval",
    stats={
        "hp": 917,
        "atk": 652,
        "def": 374,
        "spd": 104
    },
    crit_rate=0.05,
    crit_dmg=0.50
)
SERVAL.path = "Erudition"
SERVAL.element = damage.Element.LIGHTNING
SERVAL.max_energy = 100

# TODO: Implement the abilities
SERVAL.basic_attack = entities.BasicAttack()
SERVAL.skill = entities.Skill()
SERVAL.ultimate = entities.Ultimate()
SERVAL.talent = entities.Talent()
SERVAL.memosprite_skill = None
SERVAL.memosprite_talent = None
SERVAL.ascension2 = entities.AscensionTrace()
SERVAL.ascension4 = entities.AscensionTrace()
SERVAL.ascension6 = entities.AscensionTrace()
SERVAL.eidolons = [entities.Eidolon(), entities.Eidolon(), entities.Eidolon(), entities.Eidolon(), entities.Eidolon(), entities.Eidolon()]
SERVAL.stat_traces = {"ehr": 0.18, "crit_rate": 0.187, "effres": 0.10}