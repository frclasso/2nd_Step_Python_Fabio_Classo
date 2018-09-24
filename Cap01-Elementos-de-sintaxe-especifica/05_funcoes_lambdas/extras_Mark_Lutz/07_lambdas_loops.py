#!/usr/bin/env python3

import sys

showall = lambda x: list(map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])

showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(['bright\n', 'side\n', 'of\n', 'life\n'])


# showall = lambda x:[print(line, end='') for line in x]
# showall = lambda x: print(*x, sep='', end='')