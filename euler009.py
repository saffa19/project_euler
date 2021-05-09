#!/usr/bin/env python
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time

start = time.perf_counter()

def triplet(i):
    for a in range(1,i):
        for b in range(a,i):
            sq_prod = a**2 + b**2
            for c in range(b,i):
                if c**2 == sq_prod and (a+b+c) ==1000:
                    return a,b,c,sq_prod, a*b*c

print(triplet(1000))

print(time.perf_counter()-start)