#!/usr/bin/env python
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import time
import math

start = time.perf_counter()

def is_prime(a):
    # tests whether n is a multiple of any integer between 2 and sqrt(n).
    for p in primes:
        if a % p == 0:
            return False
        if p > math.sqrt(a):
            break
    return True

primes = [2]
i = 3

while len(primes) < 10001:
    if is_prime(i):
        primes.append(i)
    i+=2

print(primes[10000])
print(time.perf_counter()-start)