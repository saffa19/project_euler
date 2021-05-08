#!/usr/bin/env python
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''
import time
import math
start = time.perf_counter()

n = 600851475143 
p = 2

print("n:", n)

while n >= p * p:
    if n % p == 0:
        print(p)
        n = n/p
    else:
        p = p + 1
print(n)

print(time.perf_counter()-start)