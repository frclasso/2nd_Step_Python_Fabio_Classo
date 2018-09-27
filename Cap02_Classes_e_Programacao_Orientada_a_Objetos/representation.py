#!/usr/bin/env python3


class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: the number of bunnies is {self._n}'

    def __str__(self):
        return f'str: the number of bunnies id {self._n}'


x = bunny(47)
#print(repr(x))
print((x))  # RETIRANDO REPR, DA PREFERENCIA PARA STRING METHOD

# print(chr(128406) * 10)
# print(chr(128527) * 10)  # Emojis http://graphemica.com/



"""Para mais informacoes e exemplos de Funcoes Built-in acessem:
   https://docs.python.org/3/library/functions.html
"""