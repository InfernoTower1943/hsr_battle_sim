from base_logic import abilities, entities
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
    crit_dmg=0.50,
    star_level=4,
)

SERVAL.path = "Erudition"
SERVAL.element = damage.Element.LIGHTNING
SERVAL.max_energy = 100

# TODO: Implement the abilities
SERVAL.basic_attack = abilities.BasicAttack()
SERVAL.skill = abilities.Skill()
SERVAL.ultimate = abilities.Ultimate()
SERVAL.talent = abilities.Talent()
SERVAL.memosprite_skill = None
SERVAL.memosprite_talent = None
SERVAL.ascension2 = abilities.AscensionTrace()
SERVAL.ascension4 = abilities.AscensionTrace()
SERVAL.ascension6 = abilities.AscensionTrace()
SERVAL.eidolons = [abilities.Eidolon(), abilities.Eidolon(), abilities.Eidolon(), abilities.Eidolon(), abilities.Eidolon(), abilities.Eidolon()]
SERVAL.stat_traces = {"ehr": 0.18, "crit_rate": 0.187, "effres": 0.10}