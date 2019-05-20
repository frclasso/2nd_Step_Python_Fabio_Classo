#!/usr/bin/env/ python3
# -*-coding:utf-8 -*-


class Computer:
    """"Exemplo de encapsulamento"""
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price: US$ {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# alterando o preco
c.__maxprice = 1000 # Nao alterar o valor
c.sell()

# usando a funcao setter
c.setMaxPrice(2000)
c.sell()