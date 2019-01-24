05#!/usr/bin/env python3

"""List comprehension com duas condições IF"""

numDivBy3and5 = [ x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(numDivBy3and5)