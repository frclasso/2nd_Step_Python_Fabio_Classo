#!/usr/bin/env pyhon3

from decorators import do_twice


@do_twice
def say_whee():
    print("Whee!")


print(say_whee())
print(say_whee)
print(help(say_whee))
print(say_whee.__name__)


# @do_twice # se retirar o decorator imprime apenas uma vez
# def greet(name):
#     print(f'Hello, {name}!')
#
#
# print(greet('Fabio'))
#
# @do_twice
# def return_greeting(name):
#     print("Creating greeting!")
#     return f'Hi, {name}.'
#
# hi_adam = return_greeting('Adam')
# print(hi_adam)

