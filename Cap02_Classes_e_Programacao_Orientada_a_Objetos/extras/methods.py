#!/usr/bin/env python3

# -*-coding: utf-8 -*-


class Papagaio:

    # atributo de classe
    species = "bird"

    # atributo de instancia
    def __init__(self, name , age):
        self.name = name
        self.age = age

    # metodo de instancia( instance method)
    def sing(self, song):
        return "{} sings: {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instanciando objetos
blu = Papagaio('Blu', 10)
woo = Papagaio('Woo', 15)

# chamando os metodos de instancia
print(blu.sing("'Happy day'"))
print(blu.dance())