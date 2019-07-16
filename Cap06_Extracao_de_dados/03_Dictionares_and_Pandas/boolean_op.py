#!/usr/bin/env python3

import numpy as np

# Body mass index(BMI)
bmi = np.array([21.852, 20.975, 21.75, 24.747, 21.441])

print(bmi > 21) # [ True False  True  True  True]

# Usando operadores logicos, logical_and, logical_or, logical_not
print(np.logical_and(bmi > 21, bmi < 22)) # [ True False  True False  True]
# Exibindo os valores
print(bmi[np.logical_and(bmi > 21, bmi < 22)]) # [21.852 21.75  21.441]
