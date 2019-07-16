

height = [1.73, 1.68, 1.84, 1.89, 1.79]
weight =[65.9, 70.3, 80.4, 56.6, 70.2]

#print(weight/height ** 2)

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

imc = np_weight / np_height ** 2
#print(imc)

#print(imc < 25)

np_2D = np.array(
    [
        [1.73, 1.68, 1.84, 1.89, 1.79],
        [65.9, 70.3, 80.4, 56.6, 70.2]
    ]
)

# print(np_2D.shape)
# print(np_2D[0, 0])

print(np.mean(weight))
print(np.median(weight))