#!/usr/bin/env python3


def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4  # Defined name function

L = [f1, f2, f3]  # Reference by name

for f in L:
    print(f(2))  # Prints 4,8,16


print(L[0](3))  # Imprime 9