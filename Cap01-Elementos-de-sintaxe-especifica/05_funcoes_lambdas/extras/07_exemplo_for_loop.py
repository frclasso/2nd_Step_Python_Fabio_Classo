#!/usr/bin/env python3

# Usando um loop for jutamente com a função map

import sys
fullname = lambda x: list(map(sys.stdout.write, x))
f = fullname(['Wolfgang ', 'Amadeus ', 'Mozart'])
print(f)



"""
map (função, iterável, ...)

Retorna um iterador que aplica a função a cada item de iterável, produzindo os resultados. 
Se argumentos iteráveis ​​adicionais forem passados, a função deve levar muitos argumentos
e será aplicada aos itens de todos os iteráveis ​​em paralelo. Com vários iteráveis, o 
iterador é interrompido quando o menor iterável é esgotado.

Portanto, no exemplo acima, sys.stdout.write é um argumento para function e x é um item iterável,
 list, no exemplo.
"""