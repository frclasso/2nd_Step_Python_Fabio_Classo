#!/usr/bin/env python3

import math

from decorators import debug

# Apply a decorator to a Standard Library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


print(approximate_e(5))

'''In this example, you get a decent approximation to the true value 
e = 2.718281828, adding only 5 terms.'''