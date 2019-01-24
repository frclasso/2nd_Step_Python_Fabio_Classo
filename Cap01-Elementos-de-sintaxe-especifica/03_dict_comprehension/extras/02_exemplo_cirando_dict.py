#!/usr/bin/env python3

"""Vamos dizer, temos uma lista de frutas e podemos usar a compreensão de dict
para criar um dicionário com frutas, os elementos da lista como as chaves e o
comprimento de cada string como os valores."""

# definindo uma lista de frutas
fruits = ['apple','mango', 'banana', 'cherry']

# Dict comprehension cria um dicionario com o nome da fruta como chave
d = {f:len(f) for f in fruits}
print(d)

# a quantidade de caracter define o valor


# Fonte
# http://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/