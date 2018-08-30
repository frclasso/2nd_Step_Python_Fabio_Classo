#!/usr/bin/env python3

matrix = [[1,2,3],[4,5,6],[7,8,9]]

new_matrix = [[row[i] for row in matrix]for i in range(3)]
print(new_matrix)

"""Reescrevendo utilizando loops for aninhados"""
transposed = []

for i in range(3):
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


"""Criando uma matrix utilizando list comprehension"""
matrix2 = [[0 for col in range(4)] for row in range(3)]
print(matrix2)

"""Utilizando um loop for aninhado"""
matrix3 = []
for x in range(3):
    nested = []
    matrix3.append(nested)
    for row in range(4):
        nested.append(0)

print(matrix3)