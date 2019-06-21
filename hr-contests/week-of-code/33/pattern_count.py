#!/bin/python3

import sys

def patternCount(s):
    strList = list(s)
    # We can have two flags "is previous one" and "is previous zero" with which 
    # we can write if/else clause and check for characters "1" or "0" and set
    # the flags and respective counters
    isPrvOne = False
    isPrvZero = False
    count = 0
    for el in strList:
        if isPrvOne:
            if el == '1':
                isPrvOne = True
                isPrvZero = False
            elif el == '0':
                isPrvZero = True
                isPrvOne = False
            else:
                isPrvOne = False
                isPrvZero = False
        elif isPrvZero:
            if el == '0':
                isPrvOne = False
                isPrvZero = True
            elif el == '1':
                isPrvOne = True
                isPrvZero = False
                count += 1
            else:
                isPrvOne = False
                isPrvZero = False
        elif el == '1':
            isPrvOne = True
            isPrvZero = False
    return count
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
