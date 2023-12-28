
init python:
    from enum import Enum, unique

    @unique
    class Likes(Enum):
        ANAL = 'anal',
        BLOWJOB = 'blowjob',
        BEHIND = 'behind'

    @unique 
    class Vars(Enum):
        DEPRAVITY = 'depravity',
        SUGGESTIBILITY = 'suggestibility'

    @unique
    class GameCharacter(Enum):
        MC = 0
        LANDLADY = 1
        YOUNGER_ROOMMATE = 2
        OLDER_ROOMMATE = 3
        PROFESSOR = 4
        PHARMA_LAB_CEO = 5
        PHARMA_LAB_LEAD = 6
        NIGHT_GUARD = 7
        SECRETARY = 8

    class BaseCharacter(object):
        def __init__(self, id, name, image):
            self._id = id
            self._name = name
            self._image = image
            self._vars = {}
            self._booleans = {}
            self._traits = {}

        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @property
        def image(self):
            return self._image

        def get_var(self, name):            
            return self._vars[name] if name in self._vars else None

        def set_var(self, name, value):
            self._vars[name] = value

        def increment_var(self, name, value):
            self._vars[name] = self._vars[name] + value      

        def decrement_var(self, name, value):
            self._vars[name] = self._vars[name] + value      

        def is_true(self, name):
            return self._booleans[name] if name in self._booleans else false

        def set_bool(self, name, value):
            assert(isinstance(value, bool)), "set_bool only accepts booleans"
            self._booleans[name] = value

        @property
        def traits(self):
            return list(filter(lambda x: (self._traits[x]["hidden"] == False and self._traits[x]["value"] > 0), self._traits.keys())) 

        @traits.setter
        def set_traits(self, traits, hidden = False):
            self._traits = self._traits or []
            for trait in traits:
                if trait in self._traits:
                    self.increase_trait(trait, 1)
                else:
                    self.add_trait(trait, 1, False)

        @property
        def hidden_traits(self):
            return list(filter(lambda x: (self._traits[x]["hidden"] == True and self._traits[x]["value"] > 0), self._traits.keys())) 


        @hidden_traits.setter 
        def set_hidden_traits(self, traits):
            self.set_traits(traits, True)


        def add_trait(self, name, value, hidden):
            if name in self._traits:
                self.increase_trait(name, value)
            else:
                self._traits[name] = {"hidden": hidden, "value": value}

        def get_trait(self, name):
            if name in self._traits:
                return self._traits[name]
            else:
                return 0

        def has_trait(self, name):
            return name in self._traits

        def increase_trait(self, name, value = 1):
            if name in self._traits:
                self._traits[name] = self._traits[name] + value
            else:
                add_trait(name, value, False)

        def __call__(self, what, **kwargs):
            return Character(self._name, image=self._image)(what, kwargs)

        