#!/usr/bin/env python
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time
from math import factorial as f

start = time.perf_counter()

print(sum([int(x) for x in str(f(100))]))

print(time.perf_counter()-start)