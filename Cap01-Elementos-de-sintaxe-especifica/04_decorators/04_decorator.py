#!/usr/bin/env python3


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

#print(ordinary())

# Vamos decorar a função ordinary
pretty = make_pretty(ordinary)
print(pretty())