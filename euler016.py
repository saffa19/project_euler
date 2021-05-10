#!/usr/bin/env python
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
import time 

start = time.perf_counter()

n = str(2**1000)
ns = 0
for i in n:
    ns += int(i)
    
print(ns)

print(time.perf_counter()-start)