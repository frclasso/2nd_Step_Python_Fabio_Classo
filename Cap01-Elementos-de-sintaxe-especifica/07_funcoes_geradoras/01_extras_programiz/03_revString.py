#!/usr/bin/env python3


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


for char in rev_str('Python'):
    print(char)