
init python:
    from enum import Enum, unique

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

        def __call__(self, what, **kwargs):
            return Character(self._name, image=self._image)(what, kwargs)
