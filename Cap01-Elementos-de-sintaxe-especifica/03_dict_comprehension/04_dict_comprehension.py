#!/usr/bin/env python3

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict1_comp = {k:v for (k, v) in dict1.items() if v > 2}
print(dict1_comp)