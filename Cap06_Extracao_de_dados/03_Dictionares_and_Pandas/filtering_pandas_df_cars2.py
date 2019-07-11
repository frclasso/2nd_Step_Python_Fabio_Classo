#!/usr/bin/env python3

# Filtering Pandas DataFrames

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convertendo o codigo anterior em uma linha, nao utilizando a variavel "dr"
#dr = cars['drives_right']
sel =cars[cars['drives_right']]

# Print sel
print(sel)