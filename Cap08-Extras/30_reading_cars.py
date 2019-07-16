#!/usr/bin/env python3

import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

print(cars.head())
# print(cars[['country', 'drives_right']])
# print()
#
# print(cars.iloc[[2]])
# print(cars.iloc[[1, 6]])
# sel = cars[cars['drives_right']]
# print(sel)
# cpc = cars.iloc[:, 0]
# many_cars = cpc > 500
#
# car_maniac = cars[many_cars]
# print(car_maniac)

# for lab, row in cars.iterrows():
#     print(lab + ":" + str(row['cars_per_cap']))

for lab, row in cars.iterrows():
    cars.loc[lab, 'name_length'] = len(row['country'])
print(cars)

for lab, row in cars.iterrows():
    cars.loc[lab, 'name_length'] = row['country'].upper()
print(cars)