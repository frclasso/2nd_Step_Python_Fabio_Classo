#!/usr/bin/env python3

import glob

print(len(list(glob.iglob("/Users/fabio/Estudo/Prog/Python/2nd_Step_Python_Fabio_Classo/*/*.py", recursive=True))))

print()
print(sum(1 for i in glob.iglob("/Users/fabio/Estudo/Prog/Python/2nd_Step_Python_Fabio_Classo/*.py")))

