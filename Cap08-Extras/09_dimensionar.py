#!/usr/bin/env python3

import openpyxl


wb = openpyxl.Workbook()

#print(wb.sheetnames)
sheet = wb.active
sheet['A1'] = 'Tall row'
sheet['B2'] = 'Wide column'

sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].widht = 50

wb.save('dimensions.xlsx')

print('Feito...')