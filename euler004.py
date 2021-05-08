#!/usr/bin/env python
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time

start = time.perf_counter()

a = 100
b = 100

while a <= 999:
    while b <= 999:
        c = a * b
        print(c)
        print(str(c)[0])
        if str(c)[0] == str(c)[4]:
            print(c)
        b = b + 1
    a = a + 1
    

print(time.perf_counter()-start)