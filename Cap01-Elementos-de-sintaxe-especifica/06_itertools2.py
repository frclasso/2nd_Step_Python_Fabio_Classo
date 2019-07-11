#!/usr/bin/env python3

# Itertools Part 2
import itertools

## Permutations, order matters
election = {1:'Barb', 2:'Karen', 3:'Erin'}
# for p in itertools.permutations(election):
#     print(p)

# for p1 in itertools.permutations(election.values()):
#     print(p1)

## Combinations: Order does not matter
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
for c in itertools.combinations(colorsForPainting, 2): # 2 elements
    print(c)
