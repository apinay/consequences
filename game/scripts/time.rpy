
init python:
    from enum import Enum, unique

    @unique
    class Weekdays(enum):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7



    class Time(object):
        def __init__(self):            
            self.day = 0
            self.hour = 0

        def weekday(self):
            return (self.day - 1) % 7 + 1

        @property
        def hour(self):
            return self.hour

        @property
        def add(self, value = 1)
            self.hour = self.hour + value
            