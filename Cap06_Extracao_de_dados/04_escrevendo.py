#!/usr/bin/env python3

import openpyxl

wb = openpyxl.Workbook()


#print(wb.sheetnames)

sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'] = "LINGUAGEM"
sheet['A2'] = "Python"
sheet['A3'] = 'Django'
sheet['A4'] = 'PHP'
sheet['A5'] = 'C#'
sheet['B1'] = 'VERSAO'
sheet['B2'] = '3.7'
sheet['B3'] = '10.1'
sheet['B4'] = '8.0'
sheet['B5'] = '1.0'


#print(sheet['A1'].value)

wb.save('linguagens.xlsx')