# Slope of a regression line
# a = r*(Sy/Sx)
# r =  Correlation coefficient, Sx = Standard deviation of x data, Sy = Standard deviation of y data.
# r is already calculated in correlation_and_regression_lines_1.py
# Standard Deviation = sqrt(variance)
# variance = (sigsum((x - mu)^2)) / len(list)
# mu = mean of list

import math

def mean(nums):
    return sum(nums)/len(nums)

def variance(nums):
    m = mean(nums)
    variance = mean([abs(n - m)**2 for n in nums])
    return variance

def standard_deviation(nums):
    stdev = math.sqrt(variance(nums))
    return stdev

def correlation(listx, listy):
    elmntPrdListXandListY = [a*b for a,b in zip(listx, listy)]
    numerator = len(listx) * sum(elmntPrdListXandListY) - sum(listx) * sum(listy)
    denominator = math.sqrt((len(listx) * sum([elx**2 for elx in listx]) - (sum(listx))**2) * (len(listy) * sum([ely**2 for ely in listy]) - (sum(listy))**2))
    pearson_coefficient = numerator / denominator
    return pearson_coefficient

# Why listx as physics, because treating Physics as the independent variable
listx = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3] # Physics
listy = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15] # History
stnd_dvtn_x = standard_deviation(listx)
stnd_dvtn_y = standard_deviation(listy)
correlation_coeff = correlation(listx, listy)
slope_of_regression_line = correlation_coeff * (stnd_dvtn_y/stnd_dvtn_x)
print("{:.3f}".format(slope_of_regression_line))