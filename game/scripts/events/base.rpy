init python:
    from enum import Enum, unique

    @unique
    class ConditionType(Enum):
        VARIABLE = "variable",
        BOOLEAN = "boolean"

    @unique 
    class Operator(Enum):
        EQUAL = "==",
        LESS = "<",
        LESS_OR_EQUAL = "=<",
        MORE = ">",
        MORE_OR_EQUAL = ">="
        TRUE = "true"
        FALSE = "false"

    class Event(object):
        def __init__(self, name, trigger_time, location, prerequisities, conditions, label, repeatable = False):
            self._name = name
            (self._day_forward, self._weekdays, self._hours) = Event.fix_trigger_time(trigger_time)
            self._location = location
            self._label = label
            self._repeatable = repeatable
            self._triggered_count = 0
            self._prerequisities = prerequisities
            self._conditions = condititions

        def __eq__(self, other):
            return isinstance(other, Location) and self._id == other.id

        def __ne__(self, other):
            return not isinstance(other, Location) or self._id != other.id

        @property
        def label(self):
            return self._label

        @property
        def happened(self):
            True if self._triggered_count > 0 else False

        def is_active(self, location, time):
            return location == self._location \
                    and (self._triggered_count == 0 or self._repeatable) \
                    and time.is_time(self._hours, self._weekdays, self._day_forward) \
                    and self._is_prerequisities_done()                

        @property
        def repeatable(self):
            return self._repeatable

        @property
        def trigger_count(self):
            return self._triggered_count

        def _is_prerequisities_done(self):
            return next((event.happened for event in events if not event.happened), True)
        
        def _is_conditions_met(self):
            def condition_met(condition):
                if condition[0] == ConditionType.VARIABLE:
                    a = condition[1].get_var(condition[2])
                    b = condition[4]
                    if condition[3] == Operator.EQUAL:
                        return a == b
                    if condition[3] == Operator.LESS:
                        return a < b
                    if condition[3] == Operator.LESS_OR_EQUAL:
                        return a <= b
                    if condition[3] == Operator.MORE:
                        return a > b
                    if condition[3] == Operator.MORE_OR_EQUAL:
                        return a >= b
                if condition[0] == ConditionType.BOOLEAN:
                    if condition[3] == Operator.TRUE:
                        return condition[1].is_true(condition[2])
                    if condition[3] == Operator.FALSE:
                        return not condition[1].is_true(condition[2])

        @staticmethod
        def fix_day_forward(day_forward):
            if day_forward == None:
                return 0
            if isinstance(day_forward, int):
                return day_forward
            raise Exception("Malformed event time trigger day forward")


        @staticmethod
        def fix_weekdays(weekdays):
            if weekdays == None:
                return {}
            if isinstance(weekdays, Enum):
                return {weekdays}
            if isinstance(weekdays, list):
                return set(weekdays)            
            raise Exception("Malformed event time trigger weekdays")

        @staticmethod
        def fix_hours(hours):
            if hours == None:
                return {}
            if isinstance(hours, list):
                return Event.unfurl_hours(hours)
            raise Exception("Malformed event time trigger hours")


        @staticmethod
        def fix_trigger_time(trigger_time):
            return (
                Event.fix_day_forward(trigger_time[0]) if trigger_time and len(trigger_time > 0) else 0,
                Event.fix_weekdays(trigger_time[1]) if trigger_time and len(trigger_time > 1) else {},
                Event.fix_hours(trigger_time[2]) if trigger_time and len(trigger_time > 2) else {}
            )

        @staticmethod
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

        @staticmethod
        def select_event(location_events, location, time):

            def add_previous(items):
                # Assign areas for probabilities between 0-1
                sum_of_prev = 0
                for item in items:
                    sum_of_prev += item[0]
                    yield (sum_of_prev, item[1])

            def get_probabilities(items):
                # Calculate weighted probabilities
                trigger_counts = [x.trigger_count for x in items] 
                sum_of_counts = sum(trigger_counts)
                weights = [(sum_of_counts - x) / sum_of_counts for x in trigger_counts]
                sum_of_weights = sum(weights)
                return [x / sum_of_weights for x in weights]            

            events = [x for x in location_events if x.is_active(location, time)]
            event_count = len(events)
            if event_count <= 1:
                return events[0] if event_count == 1 else None
            single = next((x for x in events if x.repeatable), None)
            if single:
                return single

            # We know that there is only repeatable events left and there is at least two of them            
            items =  dict(add_previous(sorted(zip(get_probabilities(events), events))))
            value = renpy.random.random()
            return next(items[x] for x in items if x >= value)[1]

            
            
                
