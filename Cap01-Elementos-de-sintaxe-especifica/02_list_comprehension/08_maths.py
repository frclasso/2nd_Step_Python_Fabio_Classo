#!/usr/bin/env python3

numbers = range(10)

newList = [x**2 for x in numbers if x % 2 == 0]
print(newList)
