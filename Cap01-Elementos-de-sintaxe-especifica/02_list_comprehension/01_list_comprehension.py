#!/usr/bin/env python3

"""Criando uma lista vazia e populando atraves de um range"""
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)

"""Utilizando list comprehension"""

new_numbers = [i for i in range(10)]
print(new_numbers)

"""Aqui realizamos uma operação matemática dentro da list comprehension"""
numbers_multiplied = [i * 2 for i in range(10)]
print(numbers_multiplied)

"""Aplicando uma condição IF"""
numPar = [i for i in range(20) if i % 2 == 0]
print(numPar)