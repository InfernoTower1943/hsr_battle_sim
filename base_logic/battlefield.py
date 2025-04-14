from base_logic.entities import *
from base_logic.equippables import *
from base_logic.events import *
from base_logic.status_effects import *

class Battlefield:
    enemies = [Enemy(), Enemy(), Enemy(), Enemy(), Enemy()]
    allies = [Character(), Character(), Character(), Character()]
    turbulence = StatusEffect()
    current_cycle = 0
    action_bar = ActionBar()

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

