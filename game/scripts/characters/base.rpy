
init python:
    from enum import Enum, unique

    @unique 
    class Traits(Enum):
        DRIVEN = "driven"
        SELF_CENTERED = "self_centered"
        EFFEMINATE = "effeminate"
        SELF_CONCIOUS = "self_conscious"
        POLYAMORY = "polyamory"
        HELPFUL = "helpful"
        STUBBORN = "stubborn"
        HONEST = "honest"
        WELL_MEANING = "well_meaning"
        GREGARIOUS = "gregarious" # Should we just change this to sociable
        BISEXUAL = "bisexual"
        MANIPULATIVE = "manipulative"
        LOYAL = "loyal"
        INNOCENT_LOOKING = "innocent_looking"
        SHY = "shy"
        INCEST = "incest"
        EX_PARTY_GIRL = "ex_party_girl"
        VAIN = "vain"
        DEVOTED_TO_FAMILY = "devoted_to_family"
        STRICT = "strict"
        BRAVE = "brave"
        EXHIBITIONIST = "exhibitionist"

    @unique
    class GameCharacter(Enum):
        MC = 0
        LAND_LADY = 1
        YOUNGER_ROOM_MATE = 2
        OLDER_ROOM_MATE = 3
        PROFESSOR = 4
        PHARMA_LAB_CEO = 5
        PHARMA_LAB_LEAD = 6
        NIGHT_GUARD = 7

    class BaseCharacter(object):
        def __init__(self, id, name, image):
            self._id = id
            self._name = name
            self._image = image
            self._vars = {}
            self._booleans = {}
            self._traits = {}
            self._hidden_traits = {}

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

        def is_true(self, name):
            return self._booleans[name] if name in self._booleans else false

        def set_bool(self, name, value):
            assert(isinstance(value, bool)), "set_bool only accepts booleans"
            self._booleans[name] = value

        @property
        def traits(self):
            list(filter(lambda x: (self._traits[x] > 0), self._traits.keys()))

        def get_trait(self, name):
            if name in self._traits:
                return self._traits[name]
            else if name in self._hidden_traits:
                return self._hidden_traits[name]
            else:
                return 0

        def has_trait(self, name):
            return name in self._traits or name in self._hidden_traits

        def __call__(self, what, **kwargs):
            return Character(self._name, image=self._image)(what, kwargs)

        