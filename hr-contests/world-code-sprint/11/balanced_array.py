#!/bin/python3

import sys

def solve(a):
    first_list_sum = sum(a[len(a)//2:])
    second_list_sum = sum(a[:len(a)//2])

    return abs(first_list_sum - second_list_sum)

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a)
print(result)
