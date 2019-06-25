#!/usr/bin/env python3

# template
# wb = Workbook

import openpyxl

wb = openpyxl.Workbook()  # carrega a planilha na memoria

sheet = wb.active

sheet.title = 'Folha 1'

print(wb.sheetnames)
wb.save('teste.xlsx')
