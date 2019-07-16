#!/usr/bin/env python3

import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010, 2100]
population = [2.519, 3.692, 5.263, 6.972, 10.850]  # billions



# add more data
year = [1800, 1850, 1900] + year
population = [1.0, 1.262, 1.650] + population

plt.plot(year, population) # traça a linhaDataCamp/02_matplotlib/02_exemplo_population.py:10
plt.scatter(year, population)  # insere as bolinhas

plt.xlabel('Year')
plt.ylabel('Population')
plt.title("World Population Projections")
plt.yticks([0,2,4,6,8,10], # inicia o eixo y com zero
           ['0', '2B', '4B', '6B', '8B', '10B']) # add B ao lado do numero

plt.show()