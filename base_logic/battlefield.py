from base_logic.entities import *
from base_logic.equippables import Entity, Enemy, Ally, Character, Summon
from base_logic.events import *
from base_logic.status_effects import *

class Battlefield:
    enemies = [Enemy(), Enemy(), Enemy(), Enemy(), Enemy()]
    allies = [Character(), Character(), Character(), Character()]
    turbulence = StatusEffect()
    current_cycle = 0
    action_bar = ActionBar()
    active_abilities = tuple()

    def __init__(self, enemies=None, allies=None, turbulence=None, action_bar=None):
        if enemies is not None:
            self.enemies = enemies
        else:
            self.enemies = [Enemy() for _ in range(5)]
        if allies is not None:
            self.allies = allies
        else:
            self.allies = [Character() for _ in range(4)]
        if turbulence is not None:
            self.turbulence = turbulence
        else:
            self.turbulence = StatusEffect()
        if action_bar is not None:
            self.action_bar = action_bar
        else:
            self.action_bar = ActionBar()
        self.current_cycle = 0
        self.action_bar = ActionBar()

    def _update_entities(self):
        # TODO: Triggers when summon spawns/despawns, or character dies, or enemy dies/spawns
        # Will include updating the enemy and ally pools, and the action bar (AV).
        self._update_abilities()

    def _update_abilities(self):
        # TODO: Triggers when the ability pool is updated.
        active_abilities = []
        for ally in self.allies:
            current_ally_abilities = ally.get_abilities()
            active_abilities.extend(current_ally_abilities)
        for enemy in self.enemies:
            current_enemy_abilities = enemy.get_abilities()
            active_abilities.extend(current_enemy_abilities)
        self.active_abilities = tuple(active_abilities)

    def add_entity(self, entity):
        if isinstance(entity, Enemy):
            self.enemies.append(entity)
        elif isinstance(entity, Ally):
            self.allies.append(entity)
        else:
            raise ValueError("Entity must be an instance of Enemy or Ally.")
        self._update_entities()
        self._update_abilities()