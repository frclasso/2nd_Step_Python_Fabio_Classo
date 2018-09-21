#!/usr/bin/env python3

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Dobrando os valores
valorDobrado = {k:v*2 for(k,v) in dict1.items()}
print(valorDobrado)

# Alterando valor da chave

chaveDobrada = {k*2:v for (k,v) in dict1.items()}
print(chaveDobrada)