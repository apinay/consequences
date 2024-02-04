
init python:
    from util import weekday

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



            

            