#!/usr/bin/env python
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

import time

start = time.perf_counter()

words = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}

sum = 0

def convert(n):
    if n < 20:
        w = str(words[n])
        return w, len(w)
    elif 20 <= n < 100:
        if n % 10 == 0:
            w = words[n]
            return w, len(w)
        else:   
            u = n % 10
            t = n // 10 * 10
            w = words[t]+words[u]
            return w, len(w)
    elif 100 <= n < 1000:
        u = n % 10
        tt = n % 100
        h = n // 100
        if tt > 20:
            t = tt // 10 * 10
            w = words[h]+words[100]+words[t]+words[u]
        else:
            t = tt
            w = words[h]+words[100]+words[t]
        if t > 0 or u > 0:
            w += 'and'
        return w, len(w)
    elif n == 1000:
        th = n // 1000
        w = words[th] + words[n]
        return w, len(w)

for i in range(1,1001):
    res = convert(i)
    sum += res[1]

print(sum)

print(time.perf_counter()-start)