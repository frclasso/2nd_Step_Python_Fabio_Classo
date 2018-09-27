#!/usr/bin/env python3

# -*-coding:utf-8 -*-


class Parrot:
    """Exemplo de polimorfismo"""
    def fly(self):
        print('Parrot can fly!!')

    def swim(self):
        print('Parrot can not swim!')


class Penguin:

    def fly(self):
        print('Penguin can not fly!')

    def swim(self):
        print("Penguin can swin!!")


# interface comum
def flying_test(bird):
    bird.fly()

def swim_test(passaro):
    passaro.swim()

# instanciando objetos
blu = Parrot()
peggy = Penguin()

# passando o objeto
flying_test(blu)
flying_test(peggy)
swim_test(blu)
swim_test(peggy)