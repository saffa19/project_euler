#!/usr/bin/env python
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time

start = time.perf_counter()

max = 0

for a in range(100,1000):
    for b in range(100,1000):
        c = a * b
        
        second_half = str(c)[len(str(c))//2:]
        
        if str(c)[:len(str(c))//2] == second_half[::-1] and max < c:
            print(a,b,c)
            max = c
        
    

print(time.perf_counter()-start)