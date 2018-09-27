#!/usr/bin/env python3

# -*-coding:uff-8-*-


class ComplexNumber:
    """Deletando atributos e objetos"""
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))


# instanciando objeto
c1 = ComplexNumber(2,3)

"""deletando atributo 'imag' ## descomente as duas linhas abaixo, comente-as em seguida."""
#del c1.imag
c1.getData()
"""output: AttributeError: 'ComplexNumber' object has no attribute 'imag'"""

""" deletando metodo getData() ## descomente as duas linhas abaixo, comente-as em seguida."""
#del ComplexNumber.getData
#c1.getData()
""" output: AttributeError: 'ComplexNumber' object has no attribute 'getData'"""

""" deletando o objeto em si  ## descomente as duas linhas abaixo, comente-as em seguida."""
del c1
c1

""" output: NameError: name 'c1' is not defined"""