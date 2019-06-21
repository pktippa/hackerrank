# To compute Karl Pearson's coefficient of correlation
# http://www.statisticshowto.com/how-to-compute-pearsons-correlation-coefficients/

import math

# Given list of values as per the problem statement
listx = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
listy = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Pearson Coefficition
# r = (n*sigsum(x*y) - sigsum(x)*sigsum(y)) / (sqrt((n*sigsum(x^2) - (sigsum(x))^2) * (n*sigsum(y^2) - (sigsum(y))^2)))
# n is size of list

# element-wise multiplication/product of two lists
elmntPrdListXandListY = [a*b for a,b in zip(listx, listy)]
numerator = len(listx) * sum(elmntPrdListXandListY) - sum(listx) * sum(listy)
denominator = math.sqrt((len(listx) * sum([elx**2 for elx in listx]) - (sum(listx))**2) * (len(listy) * sum([ely**2 for ely in listy]) - (sum(listy))**2))
pearson_coefficient = numerator / denominator
print("{:.3f}".format(pearson_coefficient))