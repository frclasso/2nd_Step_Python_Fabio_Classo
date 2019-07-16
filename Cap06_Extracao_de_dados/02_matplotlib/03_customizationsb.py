#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
from population_data import gdp_cap, life_exp, pop, col

# plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) *2)
plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) *2, c=col, alpha=0.8)  # insert colors

plt.xscale('log')
plt.xlabel('GDP per Capta[in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
plt.grid(True)

plt.show()