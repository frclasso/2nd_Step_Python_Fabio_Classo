#!/usr/bin/env python3

# -*-coding:utf-8-*-


class Papagaio:

    # atributo de classe
    species = "bird"
    size = 'grande'

    # atributo de instancia
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings: {}".format(self.name, song)

    def dance(self):
        return '{} is now dancing'.format(self.name)


# instanciando objetos
blu = Papagaio('Blu', 10)
woo = Papagaio('Woo', 15)
ze= Papagaio('ZeCarioca', 20)

# acessando atributos de classe
# print("Blu is a {} and size {}.".format(blu.__class__.species, blu.size))
# print("Woo is a {} and size {}.".format(woo.__class__.species,woo.size ))
# print('Ze is a {} and size {}'.format(ZeCarioca.__class__.species, ZeCarioca.__class__.size))

# acessando atributos de objetos
print("{} is {} years old".format(blu.name, blu.age))
print(blu.sing('Happy Day'))
print(blu.dance())
print(ze.sing('Olele olala'))
print(ze.dance())
print("{} is {} years old".format(woo.name, woo.age))
print("{} is {} years old".format(ze.name, ze.age))