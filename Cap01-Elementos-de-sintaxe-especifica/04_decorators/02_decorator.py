#!/usr/bin/env python3


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc,3))

print(operate(dec, 3))