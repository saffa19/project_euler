#!/usr/bin/env python
'''
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 285 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import time

start = time.perf_counter()

def susq(lim):
    ret = 0
    for i in range(1,lim+1):
        ret = ret + i**2
    return ret

def sqsu(lim):
    ret = 0
    for i in range(1,lim+1):
        ret = ret + i
    return ret**2

print(sqsu(100)- susq(100))

print(time.perf_counter()-start)