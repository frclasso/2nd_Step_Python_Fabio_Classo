#!/usr/bin/env python3

import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Um par de colchetes [] retorna um Pandas Series
# dois pares de colchetes retorna um Pandas DataFrame

# imprimindo country
# print(cars['country'])
# print()
# print(cars[['country']])
# print()
# print(cars[['country', 'drives_right']])
#
#
#
print(cars[0:3])
print(cars[:])
print()

# loc e iloc
# loc é baseado em nomes
# iloc em indices inteiros


print(cars.iloc[[2]])
print()
print(cars.iloc[[1, 6]])
print()

#\print(cars.loc[['AUS', 'EG']])  # Erro
print(cars.iloc[3,0]) # India
print()
print(cars.iloc[[3,4], 0]) # [[IN, RU[, cars_per_car]
print()
print(cars.iloc[[3,4], [0,1]]) # [IN, RU],[cars_per_cap, country]

print()
print(cars.loc[:, 'country'])

print()
print(cars.iloc[:, 1])

print()
print(cars.loc[:, ['country', 'drives_right']])
print()
print(cars.iloc[:, [1, 2]])