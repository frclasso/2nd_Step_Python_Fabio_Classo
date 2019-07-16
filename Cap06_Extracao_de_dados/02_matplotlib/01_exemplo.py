#!/usr/bin/env python3

import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]  # billions

plt.plot(year, population) # traça a linha
plt.scatter(year, population)  # insere as bolinhas
plt.show()