#!/usr/bin/env python3

import pandas as pd
brics = pd.read_csv('brics.csv', index_col=0)


''' Select countries with area over 8 million km2
    1 - select area column
        
        brics['area'], alternatives => brics.loc[:, 'area'] or brics.iloc[:, 2]
        
    2 - Do comparison on area column
    
        brics['area'] > 8
        is_huge = brics['area'] > 8
        
    3 - use results to select countries
        brics[is_huge]
'''

is_huge = brics.iloc[:,2] > 8
print(brics[is_huge])

print()
# or
# print(brics[brics.iloc[:,2]>8])
#
# print()

import numpy as np
print(np.logical_and(brics.iloc[:,2] > 8, brics.iloc[:,2] < 10))
print()

print(brics[np.logical_and(brics.iloc[:,2] > 8, brics.iloc[:,2] < 10)])
