# To estimate a label(y) from given feature(x) for a linear regression we need Yintercept and Slope of line.
# y = mx + c, m = slope of line, c = y intercept.
# Y intercept of line
# Yintercept = Ybar - (slope)(Xbar)
# Ybar = mean(Y), Xbar = mean(X)
# Slope is already calculated in correlation_and_regression_lines_2.py

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
mean_y = mean(listy)
mean_x = mean(listx)
y_intercept = mean_y - (slope_of_regression_line * mean_x)
# Now we have to predict the label for feauture X physics value 10
# Keep values of slope, Yintercept, x to get y in y = mx + c
predicted_y = ( slope_of_regression_line * 10) + y_intercept
print("{:.1f}".format(predicted_y))