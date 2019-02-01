#!/usr/bin/env python3
# A simple generator function


def my_gen():
    n = 1
    print("This is printed first!")
    # Generator functions contains yield statements
    yield n

    n += 1
    print("this is printed second")
    yield n

    n += 1
    print("this is printed last!")
    yield n


# Using for loop
for item in my_gen():
    print(item)