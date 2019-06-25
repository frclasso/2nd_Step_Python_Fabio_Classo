#!/usr/bin/env python3

import openpyxl

wb = openpyxl.load_workbook('balances_template.xlsx')

wb.template = True

wb.save('balances_copy.xlsx')

print('Feito...')