from calendar import week
from enum import Enum
from dataclasses import dataclass

class TemporalFrequencies(Enum):
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    SEASON = 'season'
    YEAR = 'year'

class Units(Enum):
    WATT = 'watt'
    KILOWATT = 'kilowatt'
    WATTHOUR = 'watthour'
    KILOWATTHOUR = 'kilowatthour'
