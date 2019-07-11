#!/usr/bin/env python3

import statistics

agesData = [10,13,14,12,11,10,11,10,15]

print(statistics.mean(agesData)) # Average
print(statistics.median(agesData)) # Median point
print(statistics.mode(agesData)) # Most frequently item

print(statistics.variance(agesData)) # Variance
print(statistics.stdev(agesData))

import math
print(math.sqrt(statistics.variance(agesData)))  #sqr variance == stdev

