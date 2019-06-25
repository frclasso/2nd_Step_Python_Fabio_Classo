

# arquivos excel

# Openpyxl

#import openpyxl

# pandas
import pandas as pd

modo1 = pd.read_excel('battledeath.xlsx')   # csv mesmos comandos
#print(modo1)
# print(modo1.info())
# print(modo1.head())
# print(modo1.tail())
# print(modo1.describe())
# print(modo1.columns)
# print(modo1[2002])
# modo1 =modo1.sort_values('War, age-adjusted mortality due to',
#                         ascending=False)
# modo1 = modo1.reset_index(drop=True)
# print(modo1)

print(modo1.sum(numeric_only=True))

# modo2 =pd.ExcelFile('battledeath.xlsx')
#
# print(modo2.sheet_names)
# print(modo2.parse('2002', index_col=0))



