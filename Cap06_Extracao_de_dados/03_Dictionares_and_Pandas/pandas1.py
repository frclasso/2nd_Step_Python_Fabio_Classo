#!/usr/bin/env python3

import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Marroco', 'Egypt']
dr = [True, False, False, False, True, True,True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# crie um dionario my_dict com as chaves: country, drives_right,    cars_per_cap

my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# construindo um DataFrame para cars a partir de my_dict

cars = pd.DataFrame(my_dict)

print(cars)

print()
# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# defnindo row_labels como indice
cars.index = row_labels
print(cars)