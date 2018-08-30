#!/usr/bin/env python3

""" Laço for aninhado"""
lista = []
for i in range(3):
    for j in range(3):
        lista.append((i, j))
print(lista)

'''Fazendo o mesmo com list comprehensions aninhados'''
lista2 = [(i,j) for i in range(3) for j in range(3)]
print(lista2)