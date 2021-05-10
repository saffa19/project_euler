#!/usr/bin/env python
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import time
import math
from algorithms import factors_list as f

start = time.perf_counter()

a = []
t = 0
for i in range(1,10000):
    fi = f(i)
    if len(fi) > 2:
        fis = sum(fi)
        for j in range(1,10000):
            ji = f(j)
            if i != j and len(ji) > 2:
                jis = sum(ji)
                if i == jis and fis == j and i not in a and j not in a:
                    print(i, 'is amicable with', j)
                    a.append(i)
                    a.append(j)
                    t += i+j

print(t)

print(time.perf_counter()-start)