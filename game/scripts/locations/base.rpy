
init python:
    from enum import Enum, unique
    from util import fix_accessible_time

    @unique
    class Place(Enum):
        CITY_MAP = 1,
        HOME_MC_ROOM = 2,
        HOME_KITCHEN = 3,
        HOME_LANDLADY_ROOM = 4,
        HOME_YOUNGER_ROOMMATE_ROOM = 5,
        HOME_OLDER_ROOMMATE_ROOM = 6,
        PHARMA_RECEPTION = 7,
        PHARMA_LAB = 8,
        PHARMA_STORAGE_ROOM = 9,
        PHARMA_GUARD_ROOM = 10,
        PHARMA_INCINERATOR = 11

    class LocationConfig(object):
        def __init__(
            self, 
            icon_morning=None, icon_day=None, icon_evening=None, icon_night=None,
            bg_morning=None, bg_day=None, bg_evening=None, bg_night=None, bg_default=None
            accessible_hours=["06-24"]
            accessible_days='*'
            default_event=None):
            
            self.icon_morning = icon_morning
            self.icon_day = icon_day
            self.icon_evening = icon_evening
            self.icon_night = icon_night
            self.bg_morning = bg_morning
            self.bg_day = bg_day
            self.bg_evening = bg_evening
            self.bg_night = bg_night
            self.accessible = fix_accessible_time(accessible_days, accessible_hours)
            self.default_event = default_event


    class Location(object):
        def __init__(self, id, name, config):
            self._id = id
            self._name = name
            self._config = config            
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
        def accessible_locations(self):
            return self._accessible_locations
        
        def is_accessible(self, time):
            time.is_time(self._config.accessible.

        def background(self, time):
            if self._config.bg_night and (time < 6 or time => 21):
                return._config.bg_night
            if self._config.bg_morning and time => 6 and time < 10:
                return self._config.bg_morning
            if self._config.bg_day and time >= 10 and time < 16:
                return self._config.bg_day
            if self._config.bg_evening and time >= 16 and time < 22:
                return self._config.bg_evening
            if self.config.bg_default:
                return self.config.bg_default
            return img_black

        def icon(self, time):
            if self._config.icon_night and (time < 6 or time => 21):
                return._config.icon_night
            if self._config.icon_morning and time => 6 and time < 10:
                return self._config.icon_morning
            if self._config.icon_day and time >= 10 and time < 16:
                return self._config.icon_day
            if self._config.icon_evening and time >= 16 and time < 22:
                return self._config.icon_evening
            if self.config.icon_default:
                return self.config.icon_default
            return img_black

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

