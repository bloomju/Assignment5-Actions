import math
from datetime import date


def firstrun():
    return "success"


def areaFromRadius(rad):
    return math.pi * (rad*rad)


def firstLastElement(myList):
    return [myList[0], myList[-1]]


def numDays(date1, date2):
    return abs((date2-date1).days)
