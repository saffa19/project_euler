#!/usr/bin/env python
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
import time
from math import factorial as f

start = time.perf_counter()

def choose(n,k):
    return (f(n)//(f(k)*f(n-k)))

print(choose(40,20))


print(time.perf_counter()-start)