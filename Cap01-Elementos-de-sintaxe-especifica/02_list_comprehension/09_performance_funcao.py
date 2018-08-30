#!/usr/bin/env python3

"""Comparando a performance através do tempo de execução, entre
loop FOR aninhados versus List comprehension."""
import timeit

numbers = range(10)
new_list = []


def power_two(numbers):
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n**2)
    return new_list


print("Utilizando um loop For")
print(timeit.timeit('power_two(numbers)', globals=globals(), number=10000))


print('Utilizando List Comprehension')
print(timeit.timeit('[n**2 for n in range(10) if n % 2 == 0]',number=1000))