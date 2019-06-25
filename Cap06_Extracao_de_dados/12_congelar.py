#!/usr/bin/env python3

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']
sheet.freeze_panes = 'A2'  # Error

wb.save('congelada.xlsx')

print('Feito...')