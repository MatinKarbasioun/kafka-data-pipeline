from enum import IntEnum


class Interval(IntEnum):
    ONE_MINUTE = 0
    THREE_MINUTE = 1
    FIFTEEN_MINUTE = 2
    THIRTY_MINUTE = 3
    ONE_HOUR = 4
    TWO_HOURS = 5
    FOUR_HOURS = 6
    SIX_HOURS = 7
    EIGHT_HOURS = 8
    TWELVE_HOURS = 9
    ONE_DAY = 10
    THREE_DAYS = 11
    ONE_WEEK = 12
    ONE_MONTH = 13
