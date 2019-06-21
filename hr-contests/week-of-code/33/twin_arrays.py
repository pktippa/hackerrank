#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    # Calculating the minimum values of two arrays
    minInAr1 = min(ar1)
    minInAr2 = min(ar2)
    # Infinite loop
    while True:
        # Getting indexes of min values of two arrays
        indices_of_min_ar1 = [i for i, x in enumerate(ar1) if x == minInAr1]
        indices_of_min_ar2 = [i for i, x in enumerate(ar2) if x == minInAr2]
        # if indices length or not same, then there is atleast 1 combination of min sum value
        if len(indices_of_min_ar1) > 1 or len(indices_of_min_ar2) > 1:
            return minInAr1 + minInAr2
        # else if both indexes are not equal then also we lead to min sum value
        elif indices_of_min_ar1[0] != indices_of_min_ar2[0]:
            return minInAr1 + minInAr2
        # Now indexes are same, this becomes tricky now.
        else:
            # Compare if min value in ar1 is less than min value in ar2
            # then remove the min value in ar1 and continue with loop
            if minInAr1 < minInAr2:
                ar1.remove(minInAr1)
                minInAr1 = min(ar1)
            # if min values of both ar1 and ar2 are same, then compare the
            # next level of min values as we did above way
            elif minInAr1 == minInAr2:
                # Copying ar1 and ar2 to temps
                tmp1 = ar1[:]
                tmp2 = ar2[:]
                # Removing min values from both arrays
                tmp1.remove(minInAr1)
                tmp2.remove(minInAr2)
                # if min value of tmp1 is less than min value of tmp2
                # then remove the min value in ar1 and continue with loop
                if min(tmp1) < min(tmp2):
                    ar1.remove(minInAr1)
                    minInAr1 = min(ar1)
                # if min values of both tmp1 and tmp2 are same, then remove
                # both min values of ar1 and ar2 should be removed.
                elif  min(tmp1) == min(tmp2):
                    ar1.remove(minInAr1)
                    minInAr1 = min(ar1)
                    ar2.remove(minInAr2)
                    minInAr2 = min(ar2)
                # if min value of tmp1 is greater than min value of tmp2
                # then remove the min value in ar2 and continue with loop
                else:
                    ar2.remove(minInAr2)
                    minInAr2 = min(ar2)
            # if min value in ar1 is greater than min value in ar2
            # then remove the min value in ar1 and continue with loop
            else:
                ar2.remove(minInAr2)
                minInAr2 = min(ar2)

n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)