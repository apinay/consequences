
init python:
    from enum import Enum, unique

    @unique
    class Place(Enum):
        HOME_MC_ROOM = 1,
        HOME_KITCHEN = 2,
        HOME_LANDLADY_ROOM = 3,
        HOME_YOUNGER_ROOMMATE_ROOM = 4,
        HOME_OLDER_ROOMMATE_ROOM = 5,
        PHARMA_RECEPTION = 6,
        PHARMA_LAB = 7,
        PHARMA_STORAGE_ROOM = 8,
        PHARMA_GUARD_ROOM = 9,
        PHARMA_INCINERATOR = 10


    class Location(object):
        def __init__(self, id, name, icon, background):
            self._id = id
            self._name = name
            self._icon = icon
            self._background = background
            self._events = []

        def __eq__(self, other):
            return isinstance(other, Location) and self._id == other.id


        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        @property
        def background(self):
            return self._background

        def get_events(self, time):
            [event.get_labels(self, time) for event in self._events]
