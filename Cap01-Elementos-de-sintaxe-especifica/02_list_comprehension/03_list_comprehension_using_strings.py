#!/usr/bin/env python3

"""Criando uma lista utilizando list comprehension e strings"""

shark_letters = []
for letter in 'shark':
    shark_letters.append(letter)

print(shark_letters)

shark_letters2 = [letter for letter in 'shark']
print(shark_letters2)