#!/usr/bin/env python3

divided = []

# Utilizando um laço for
for x in range(100):
    if x % 2 == 0:
        if x % 6 == 0:
            divided.append(x)

print(divided)

# Utilizando list comprehension
divided_listC = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
print(divided_listC)