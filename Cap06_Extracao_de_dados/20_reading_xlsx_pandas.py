#!/usr/bin/env python3

import pandas as pd

file = 'Road-Accident-Safety-Data-Guide.xlsx'

xl = pd.ExcelFile(file)

for x in xl.sheet_names:
    print(x)
print()

#df1 = xl.parse('Day_of_week')
df1 = xl.parse('Police Force')
print(df1.head())
#print(df1.tail())
#print(df1.info())
#print(df1.keys()) # colunas
#print(df1.columns)