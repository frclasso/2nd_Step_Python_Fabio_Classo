#!/usr/bin/env python3

import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
# for lab, row in cars.iterrows():
#     print(lab + ": " + str(row["cars_per_cap"]))

# Adding column "name_length"
for lab, row in cars.iterrows():
    cars.loc[lab, "name_length"] = len(row["country"])
#print(cars)

for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()
print(cars)

"""Using iterrows() to iterate over every observation of a Pandas DataFrame is easy to 
understand, but not very efficient. On every iteration, you're creating a new Pandas Series.

If you want to add a column to a DataFrame by calling a function on another column,
 the iterrows() method in combination with a for loop is not the preferred way to go. 
 Instead, you'll want to use apply()"""
print()

# mesmo resultado
cars["COUNTRY"] = cars['country'].apply(str.upper)
print(cars)