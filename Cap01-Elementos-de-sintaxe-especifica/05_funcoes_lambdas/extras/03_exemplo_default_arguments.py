#!/usr/bin/env python3

def dados(nome, idade=40):  # argumento padrão
    return nome, idade

# print(dados('Fabio'))


mz = (lambda a='Wolfgangus', b='Theophilus', c='Mozart': a + b + c)
print(mz('Wolfgang ', 'Amadeus '))