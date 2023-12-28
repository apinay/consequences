
init python:
    import re
    from enum import Enum, unique

    hour_regex = "([0-1]?[0-9]|2[0-3])"
    # extract_range = re.compile("^{hour_regex}$|^{hour_regex}-{hour_regex}$".format(hour_regex=hour_regex))
    extract_range = re.compile("^{hour_regex}-{hour_regex}$".format(hour_regex=hour_regex))

    @unique
    class Weekday(Enum):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

    class Time(object):
        def __init__(self):            
            self._day = 0
            self._hour = 0

        @property
        def weekday(self):
            return (self._day - 1) % 7 + 1

        @property
        def hour(self):
            return self._hour

        @property
        def add(self, value = 1):
            self._hour = self._hour + value
            if self._hour > 23:                
                self._day = self._day + self._hour // 24
                self._hour = self._hour % 24
            
        def is_time(self, hours, weekdays, day_forward):
            if day_forward and self._day < day_forward:
                return False
            if weekdays and not self.weekday in weekdays:
                return False
            if hours and not self._hour in hours:
                return False
            return True



            

            