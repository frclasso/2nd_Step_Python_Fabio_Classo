#!/usr/bin/env python3

"""Comparando a performance através do tempo de execução, entre
loop FOR aninhados versus List comprehension."""
import timeit

numbers = range(10)
new_list = []

newList = [n**2 for n in numbers if n % 2 == 0]
print(newList)

print('Tempo de execução:')
print(timeit.timeit('[n**2 for n in range(10) if n % 2 == 0]',number=1000))