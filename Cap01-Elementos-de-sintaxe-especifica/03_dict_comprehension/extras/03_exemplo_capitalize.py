#!/usr/bin/env python3

"""Vamos criar um dicionário com  dict comprehension, de modo que os elementos da
 lista sejam as chaves e os elementos com a primeira letra sejam capitalizados
 como os valores."""

# definindo uma lista de frutas
fruits = ['apple','mango', 'banana', 'cherry']

d = {f:f.capitalize() for f in fruits}
print(d)






# Fonte
# http://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/