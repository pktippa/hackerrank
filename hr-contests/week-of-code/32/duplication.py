#!/bin/python3

import sys

def duplication(x):
    # Retriving the global str_s
    global str_s
    # return the required character in return.
    return str_s[x]

str_s = "0"
while len(str_s) < 1000:
    # Using double replacements
    str_s += str_s.replace('0', 'x').replace('1', '0').replace('x', '1')

# Reading number of tests
q = int(input().strip())
# Looping through tests number
for a0 in range(q):
    # taking each input
    x = int(input().strip())
    # Calling duplication function to retrieve required result
    result = duplication(x)
    # Printing result.
    print(result)
