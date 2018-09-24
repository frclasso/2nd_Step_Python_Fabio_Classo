#!/usr/bin/env python3

from decorators import repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}")


print(greet('Python'))


@repeat
def say_whee():
    print("Whee!")


print(say_whee())  # Error , TypeError: 'NoneType' object is not callable

