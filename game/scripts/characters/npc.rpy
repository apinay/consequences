

init python:    

    class NonPlayerCharacter(BaseCharacter):
        def __init__(self, id, name, image, traits, hidden_traits):
            super().__init__(id, name, image)
            self.set_var(Vars.DEPRAVITY, 0)
            self._traits = traits
            self._hidden_traits = hidden_traits

    @property 
    def depravity(self):
        return self.get_var(Vars.DEPRAVITY)

    def add_depravity(self, amount):
        self.increment_var(Vars.DEPRAVITY, amount)

    def remove_depravity(self, amount):
        self.decrement_var(Vars.DEPRAVITY, amount)

    @property 
    def suggestibility(self):
        return self.get_var(Vars.SUGGESTIBILITY)
        

    def add_suggestibility(self, amount=10):
        self.increment_var(Vars.SUGGESTIBILITY, amount)

    def remove_suggestibility(self, amount=10):
        self.decrement_var(Vars.SUGGESTIBILITY, amount)

