#!/usr/bin/env python
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import time
import algorithms as al

start = time.perf_counter()

print(sum(al.primesToInteger(2000000)))

print(time.perf_counter()-start)