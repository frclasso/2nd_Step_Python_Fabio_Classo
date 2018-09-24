#!/usr/bin/env python3

L = [lambda x: x**2,  # In line function definition
      lambda x: x**3,
      lambda x: x**4] # A list  of three callable functions

for f in L:
    print(f(2))  # Print 4,8,16

print(L[0](3))  # Resultado de 3 ao quadrado