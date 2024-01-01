
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
        def __init__(self, id, name, icon, background, default_event=None):
            self._id = id
            self._name = name
            self._icon = icon
            self._background = background
            self._events = []
            self._default_event = default_event
            self._accessible_locations = []

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

        @property
        def get_accessible_locations(self):
            return self._accessible_locations

        def add_accessible_location(self, location):
            self._accessible_locations.append(location)
            
        def add_event(self, event):
            self._events.append(event)

        def get_event(self, time):
            event = Event.select_event(self._events, self, time)
            return event if event else self._default_event if self._default_event else None

        def clean_up_events(self):
            remaining_events = [x for x in self._events if not x.happened or x.repeatable]
            self._events = remaining_events

