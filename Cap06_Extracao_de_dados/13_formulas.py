#!/usr/bin/env python3

import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = 400
sheet['A4'] = 500

sheet['A5'] = '=SUM(A1:A4)'

wb.save('formula.xlsx')
print('Feito...')