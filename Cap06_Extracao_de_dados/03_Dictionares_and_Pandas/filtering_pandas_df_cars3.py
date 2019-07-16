#!/usr/bin/env python3

# Filtering Pandas DataFrames

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# print(cars.head())
# print(cars.iloc[:, 0])  # todos os valores na primeira coluna


# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars.iloc[:, 0]  # erro com loc
many_cars = cpc > 500
#
car_maniac = cars[many_cars]
print(car_maniac)