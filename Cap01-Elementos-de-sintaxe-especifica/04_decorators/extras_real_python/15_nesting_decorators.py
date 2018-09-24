#!/usr/bin/env python3

from decorators import debug, do_twice

@debug
@do_twice
def greet(name):
    print(f"Hello, {name}")


print(greet('Python'))

# Experimente alterar a ordem dos decorators