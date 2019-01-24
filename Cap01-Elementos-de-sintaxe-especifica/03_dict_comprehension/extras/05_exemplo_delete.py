#!/usr/bin/env python3

"""Aqui nós usamos enumerate function na lista para criar tuplas de elemento de
índice e lista e usá-las para criar um dicionário com dict comprehension.
Criamos um dicionário com elementos da lista como as chaves e o índice de
elementos como os valores."""

# definindo uma lista de frutas
fruits = ['apple','mango', 'banana', 'cherry']

f_d1 = {f:f.capitalize() for f in fruits}
print(f_d1)

print()

# Agora vamos remover duas chaves e seus respectivos valores do dicionario fruits
remove_this = {'apple','cherry'}

# Deletando um par chave:valor com dict comprehension
removed = {key:f_d1[key] for key in f_d1.keys() - remove_this}
print(removed)


# Fonte
# http://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/