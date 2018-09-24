#!/usr/bin/env python3


def parent(num):
    def first_child():
        return "Hi, I'am Emma."

    def second_child():
        return "Call me Liam."

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

print(first) # Sem parenteses retorna apenas uma referência da função
print(second)

"""Note que você está retornando first_child sem os parênteses.
Lembre-se de que isso significa que você está retornando uma referência para a função
first_child. Em contraste first_child () com parênteses refere-se ao resultado
de avaliar a função. """

print(first()) # retorna o resultado da função
print(second())