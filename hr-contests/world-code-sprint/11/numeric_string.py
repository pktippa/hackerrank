#!/bin/python3

import sys

# For some of the inputs getting the runtime error.
def getMagicNumber(s, k, b, m):
    # Complete this function
    res = 0
    nums_list = []
    i = 0
    while i + k < len(s) + 1:
         nums_list.append(s[i:k+i])
         i += 1
    nums_with_base_10 = []
    while nums_list:
        num_str = nums_list.pop()
        num_ls = list(map(int, list(num_str)))
        total_sum = 0
        power_counter = 0
        while num_ls:
            total_sum += num_ls.pop() * b**power_counter
            power_counter += 1
        nums_with_base_10.append(total_sum)
    while nums_with_base_10:
        res += nums_with_base_10.pop() % m
    return res

s = input().strip()
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
