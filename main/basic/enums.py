# https://docs.python.org/3/library/enum.html

from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class ColorAuto(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

    @classmethod
    def favorite_mood(cls):
        return cls.RED

    def describe(self):
        return self.name, self.value

result = list(map(lambda c: c.name, ColorAuto))

#%%

from enum import IntEnum

Weekdays = IntEnum('Weekdays', 'sun mon tue wed thu fri sat', start=0)
weekday == Weekdays.wed
weekday_enum = Weekdays(weekday)
SUN, MON, TUE, WED, THU, FRI, SAT = range(7)