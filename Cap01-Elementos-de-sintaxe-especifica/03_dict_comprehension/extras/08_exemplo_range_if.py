#!/usr/bin/env python3

newDict = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(newDict)


# Fonte:
# https://www.geeksforgeeks.org/python-dictionary-comprehension/