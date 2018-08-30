#!/usr/bin/env python3

""" Laço for aninhado / Nested loop"""

numList = []
for x in [10,20,30]:
    for j in [2,4,6]:
        numList.append(x*j)
print(numList)

numList2 = [x * y for x in [10,20,30] for y in[2,4,6]]
print(numList2)