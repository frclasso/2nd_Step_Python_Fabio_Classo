#!/usr/bin/env python3

"""Aqui nós usamos enumerate function na lista para criar tuplas de elemento de
índice e lista e usá-las para criar um dicionário com dict comprehension.
Criamos um dicionário com elementos da lista como as chaves e o índice de
elementos como os valores."""

# definindo uma lista de frutas
fruits = ['apple','mango', 'banana', 'cherry']

d = {f:i for i, f in enumerate(fruits)}
print(d)

print()

# invertendo as posições de chaves e valores
inverted = {v:k for k, v in d.items()}
print(inverted)


# Fonte
# http://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/