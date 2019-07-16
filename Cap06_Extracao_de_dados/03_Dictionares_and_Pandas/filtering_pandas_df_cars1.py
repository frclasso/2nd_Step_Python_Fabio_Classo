#!/usr/bin/env python3

# Filtering Pandas DataFrames

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

print(sel)