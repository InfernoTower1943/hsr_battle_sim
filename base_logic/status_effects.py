class StatusEffect:
    name: str = "StatusEffect"
    effects = None

    def __init__(self, name):
        self.name = name
        # TODO: fill out the stats

    def __repr__(self):
        return f"Entity({self.name}, {self.effects})"
    
class Buff(StatusEffect):
    def __init__(self, name):
        super().__init__(name)
        self.effects = []
    
    def add_effect(self, effect):
        self.effects.append(effect)
    
    def remove_effect(self, effect):
        self.effects.remove(effect)

class Debuff(StatusEffect):
    def __init__(self, name):
        super().__init__(name)
        self.effects = []
    
    def add_effect(self, effect):
        self.effects.append(effect)
    
    def remove_effect(self, effect):
        self.effects.remove(effect)