#!/usr/bin/env python3

# -*-coding:uff-8-*-


class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{}+{}j".format(self.real, self.imag))

# criando um novo objeto ComplexNumber
c1 = ComplexNumber(2,3)

# chamando a funcao getData()
# saida: 2+3j
c1.getData()

# criando mais um objeto ComplexNumber
# e criando um novo atributo attr
c2 = ComplexNumber(5)
c2.attr = 10

# saida: (5, 0 , 10)
print((c2.real, c2.imag, c2.attr))

# no entanto c1 nao possui o atributo 'attr'
# Attibute Error: 'ComplexNumber object has no attribute 'attr'
#c1.attr
c2.getData()
