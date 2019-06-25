#!/usr/bin/env python3


import pandas

# Data Frame

df = pandas.read_csv('hrdata.csv',
                     index_col='Employee',
                     parse_dates=['Hired'],
                     header = 0,
                     names = ['Employee', 'Hired', 'Salary', 'Sick days'])

#print(df)
# salvando
df.to_csv('hrdata_modificado.csv')