#!/bin/python3
# This solution is not correct.

import sys

def getMaxMonsters(n, hit, t, h):
    count = 0;
    h.sort()
    while t > 0:
        el = h.pop(0)
        while el > 0:
            el -= hit
            t -= 1
        else:
            count += 1
    return count

n, hit, t = input().strip().split(' ')
n, hit, t = int(n), int(hit), int(t)
h = list(map(int, input().strip().split(' ')))
print(h)
result = getMaxMonsters(n, hit, t, h)
print(result)