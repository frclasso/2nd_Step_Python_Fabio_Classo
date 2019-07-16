#!/usr/bin/env python3

import numpy as np

data = np.genfromtxt('Titanic_2.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

print(np.shape(data))

print(data['Survived'])