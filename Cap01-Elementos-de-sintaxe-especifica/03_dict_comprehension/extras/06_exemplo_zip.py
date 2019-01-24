#!/usr/bin/env python3

# Iterando sobre duas lista atrasvés da função zip
keys = ['a','b', 'c', 'd', 'e']
values = [100,200,300,400,500]

# criando um dicionario
myDict = dict(zip(keys, values))
print(myDict)


# usando Dict comprehension
myDict2 = {k:v for (k,v) in zip(keys, values)}
print(myDict2)

# Fonte:
# https://www.geeksforgeeks.org/python-dictionary-comprehension/