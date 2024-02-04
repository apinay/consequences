import re
from enum import Enum, unique

@unique
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

hour_regex = "([0-1]?[0-9]|2[0-3])"    
extract_range = re.compile("^{hour_regex}-{hour_regex}$".format(hour_regex=hour_regex))

def unfurl_hours(hours):
    def process_entry(entry):
        if isinstance(entry, int) and entry < 24 and entry >= 0:
            return [entry]
        if isinstance(entry, str):
            if entry.isdigit():
                return [int(entry)]
            e_range = extract_range.match(entry)
            if e_range and e_range.lastindex == 2:
                return list(range(int(e_range[1]), int(e_range[2]) + 1))
        return None
    return set([x for xs in filter(lambda x: x is not None, [process_entry(x) for x in hours]) for x in xs])

def fix_hours(hours):
    if hours == None:
        return None
    if isinstance(hours, list):
        return unfurl_hours(hours)
    raise Exception("Malformed time trigger hours")

def fix_weekdays(weekdays):
    if weekdays == None:
        return None
    if isinstance(weekdays, str) and weekdays == '*':
        return {Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, 
                Weekday.FRIDAY, Weekday.SATURDAY, Weekday.SUNDAY}
    if isinstance(weekdays, Enum):
        return {weekdays}
    if isinstance(weekdays, list):
        return set(weekdays)            
    raise Exception("Malformed time trigger weekdays")

def fix_day_forward(day_forward):
    if day_forward == None:
        return 0
    if isinstance(day_forward, int):
        return day_forward
    raise Exception("Malformed time trigger day forward")

def fix_accessible_time(accessible_time):
    return (
        fix_weekdays(accessible_time[0]) if accessible_time and len(accessible_time) > 0 else None,
        fix_hours(accessible_time[1]) if accessible_time and len(accessible_time) > 1 else None
    )

def fix_trigger_time(trigger_time):
    return (
        fix_day_forward(trigger_time[0]) if trigger_time and len(trigger_time > 0) else 0,
        fix_weekdays(trigger_time[1]) if trigger_time and len(trigger_time > 1) else None,
        fix_hours(trigger_time[2]) if trigger_time and len(trigger_time > 2) else None
    )
