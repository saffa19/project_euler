#!/usr/bin/env python
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import time

start = time.perf_counter()

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sum = 0
score = 0

with open('p022_names.txt') as f:
    names = f.read().lower().replace('"', '').split(',')

names.sort()

for i, name in enumerate(names, 1):
    for nChar in name:
        for j, aChar in enumerate(chars, 1):
            if aChar == nChar:
                score += j
        sum += score * i
        score = 0
        
print('sum',sum)

print(time.perf_counter()-start)