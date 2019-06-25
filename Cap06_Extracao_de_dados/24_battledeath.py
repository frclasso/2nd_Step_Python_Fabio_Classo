

import pandas as pd

#battledeath.xlsx

file = 'battledeath.xlsx'
xl = pd.ExcelFile(file)

print(xl.sheet_names)

df1 = xl.parse('2004')
print(df1.head())
# print(df1.columns)
# print(df1['War(country)'])
print()

df2 = xl.parse(names=['War 2','2002'])
print(df2.head())