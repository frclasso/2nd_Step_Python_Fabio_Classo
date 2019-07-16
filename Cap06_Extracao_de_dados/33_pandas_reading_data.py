import pandas as pd

cars = pd.read_csv('cars_data.csv', index_col=0)
print(cars)
# print(cars[['countries', 'car_per_cap']])


# print(cars[0:3])
# print(cars[:])

# loc (baseada nos nomes das colunas)
# e iloc (baseada em indices numericos)

print(cars.iloc[[2]])
print(cars.iloc[[1, 6]]) # exatamente o 1 e o 6
print(cars.iloc[[1, 6], [0,1]]) # countries, drives_right

print(cars.loc[['AUS']])
print()
print(cars.loc[['US', 'EG'], ['countries', 'drives_right']])
print()

print(cars.loc[:, ['countries', 'drives_right']])
print(cars.iloc[:, [0,1]])  # todas as linhas / colunas
print(cars.iloc[:, :])

print(cars.sum(numeric_only=True))