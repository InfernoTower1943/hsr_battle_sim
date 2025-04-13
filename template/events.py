class ActionBar:
    pass

class ActionBarEvent:
    # Something happens on the action bar
    ALLY_TURN = 1
    ENEMY_TURN = 2
    ABILITY_USED = 3
    event_type = -1
    def __init__(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data

    def __str__(self):
        return f"Event(type={self.event_type}, data={self.event_data})"