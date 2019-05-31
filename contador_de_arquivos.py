#!/usr/bin/env python3

import glob

print(len(list(glob.iglob("/Users/fabio/Estudo/Prog/Python/apostila_python_modulo_2/*/*.py", recursive=True))))

print()
print(sum(1 for i in glob.iglob("/Users/fabio/Estudo/Prog/Python/apostila_python_modulo_2/*.py")))

