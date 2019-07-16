#!/usr/bin/env python3

import numpy as np

# Assign the filename: file
file = 'Titanic_2.csv'

# Import file using np.recfromcsv: d

d = np.recfromcsv(file, delimiter=',',names=True, dtype=None, encoding='utf-8')
# Print out first three entries of d
print(d[:3])
