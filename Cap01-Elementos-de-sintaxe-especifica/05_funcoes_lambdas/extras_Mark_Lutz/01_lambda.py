#!/usr/bin/env python3


def func(x,y,z): return x + y + z


f = lambda x,y,z:x+y+z

print(f'Utilizando uma função def: {func(2,3,4)}')

print(f"Utilizando lambda: {f(2,3,4)}")