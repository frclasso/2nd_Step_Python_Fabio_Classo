import pandas as pd

brics = pd.read_csv('brics.csv', index_col=0)

print(brics.head())


# Area maior 8k
#is_huge = brics.loc['area'] > 8
# is_huge = brics.iloc[:, 2] > 8
# print(brics[is_huge])

# Populacao
# pop = brics.iloc[:, 3] < 1000
# print(brics[pop])
# print()

import numpy as np
print(np.logical_and(brics.iloc[:,2] > 8, brics.iloc[:,2] < 10))
print(brics[np.logical_and(brics.iloc[:,2] > 8, brics.iloc[:,2] < 10)])
