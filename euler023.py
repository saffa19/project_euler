#!/usr/bin/env python
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot 
be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import time
from algorithms import factors_of

start = time.perf_counter()

lim = 28125
total = 0
a = []

def ab(n):
    f = factors_of(n)
    if len(f) > 1:
        s = sum(f)
        if s == n:
            return 'p'
        elif s > n:
            #print(n,s,f)
            return 'a'
        else:
            return 'd'

# for all positive integers
for i in range(1,lim+1):
    # if integer is abundant
    if ab(i) == 'a':
        # add it to the list of abundants
        a.append(i)
    # if sum of any two abundants != i
    if not any((i-x in a) for x in a):
        total += i
    if i % 100 == 0:
        print(i)
        
print(total)

print(time.perf_counter()-start)