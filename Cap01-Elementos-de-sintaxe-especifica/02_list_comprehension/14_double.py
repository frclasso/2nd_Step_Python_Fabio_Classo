#!/usr/bin/env python3


def double(x):
    return x *2


print([double(x) for x in range(10)])
print([double(x) for x in range(10) if x % 2 == 0])