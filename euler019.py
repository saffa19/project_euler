#!/usr/bin/env python
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import time

start = time.perf_counter()

months = {
    'jan': 31,
    'feb': 28,
    'mar': 31,
    'apr': 30,
    'may': 31,
    'jun': 30,
    'jul': 31,
    'aug': 31,
    'sep': 30,
    'oct': 31,
    'nov': 30,
    'dec': 31,
}

days = ['mon','tue','wed','thu','fri','sat','sun']

day = days[0]
count = 0
pointer = 0

def leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

for year in range(1900,2001):
    for month in months:
        if leap(year) and month == 'feb':
            for i in range(29):
                if day == days[6] and year > 1900:
                    if i+1 == 1:
                        count += 1
                    day = days[0]
                    pointer = 0
                else:
                    pointer += 1
                    day = days[pointer]
        else:
            for i in range(months[month]):
                if day == days[6]:
                    if i+1 == 1 and year > 1900:
                       count += 1
                    day = days[0]
                    pointer = 0
                else:
                    pointer += 1
                    day = days[pointer]

print(count)

print(time.perf_counter()-start)