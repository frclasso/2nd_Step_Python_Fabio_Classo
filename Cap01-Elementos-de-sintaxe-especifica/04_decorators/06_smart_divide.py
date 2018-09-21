#!/usr/bin/env python3


def smart_divide(func):
    def inner(a, b):
        print("I am going divide", a, "and", b)
        if b == 0:
            print("Ops, can not divide ")
            return
        return func(a,b)
    return inner


@smart_divide
def divide(a,b):
    return a/b

print(divide(2, 5))
print()
print(divide(2, 0))