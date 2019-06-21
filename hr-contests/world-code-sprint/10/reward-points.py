#!/bin/python3

import sys

# Function to retun the sum of total points
def getPoints(month1, month2, month3):
    month1 = getMonthlyPoints(month1)
    month2 = getMonthlyPoints(month2)
    month3 = getMonthlyPoints(month3)
    return month1 + month2 + month3

# Function to get monthly points
def getMonthlyPoints(month):
    month = month * 10;
    if month > 100:
        return 100
    else:
        return month

# Reading 3 months input
month1,month2,month3 = input().strip().split(' ')
# Converting into int
month1,month2,month3 = [int(month1),int(month2),int(month3)]
# Calculating total points earned.
pointsEarned = getPoints(month1, month2, month3)
print(pointsEarned)
