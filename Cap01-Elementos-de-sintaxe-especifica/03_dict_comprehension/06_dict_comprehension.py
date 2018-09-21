#!/usr/bin/env python3

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

dict1_comp = {k:v for (k, v) in dict1.items() if v > 2 if v % 2 == 0 if v % 3 == 0}
print(dict1_comp)

# Correspondente utilizando for loop

dict1_tripleCond = {}
for(k,v) in dict1.items():
    if(v > 2 and v % 2 == 0 and v % 3 == 0):
        dict1_tripleCond[k] = v

print(dict1_tripleCond)