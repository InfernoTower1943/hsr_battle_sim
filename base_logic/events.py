class Event:
    event_type = -1
    def __init__(self, event_type):
        self.event_type = event_type

class ActionBar:
    pass

class ActionBarEvent(Event):
    # Something happens on the action bar
    ALLY_TURN = 1
    ENEMY_TURN = 2
    ABILITY_USED = 3
    event_type = -1
    event_data = None
    def __init__(self, event_type, event_data):
        super().__init__(event_type)
        self.event_data = event_data

    def __str__(self):
        return f"ActionBarEvent(type={self.event_type}, data={self.event_data})"
    
class DamageTakenEvent(Event):
    # Some damage is dealt, be it real damage or toughness
    pass