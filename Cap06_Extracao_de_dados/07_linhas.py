#!/usr/bin/env python3

import openpyxl

wb = openpyxl.load_workbook('linguagens.xlsx')

sheet = wb['Sheet']

# Cell Objects
print(tuple(sheet['A1:B1']))

# Iterando
for row in sheet['A1:B5']:
    for cell in row:
        print(cell.coordinate, cell.value)
    print('----- Final da linha ----')