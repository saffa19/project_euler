#!/usr/bin/env python
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import time
import math

start = time.perf_counter()

number = 1

# lowest common multiple 
def lcm(a,b):
    return int(a*b/math.gcd(a,b))


for i in range(1,21):
    #get the lowest common multiple of the index i and the target integer
    number = lcm(number,i)


print(number)
print(time.perf_counter()-start)