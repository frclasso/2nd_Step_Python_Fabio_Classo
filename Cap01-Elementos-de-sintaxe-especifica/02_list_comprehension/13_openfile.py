#!/usr/bin/env python3

# Criando um filtro utilizando list comprehension

fh = open('test.txt', 'r')
result= [i for i in fh if 'line3' in i]
print(result)