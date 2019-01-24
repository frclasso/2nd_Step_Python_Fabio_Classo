#!/usr/bin/env python3

# usando dicionarios
key = 'square'

print({'square':(lambda x:x**2),
     'cubic':(lambda x:x**3),
     'quadratic':(lambda x:x**4)}[key](10))



# Fonte
# https://www.bogotobogo.com/python/python_functions_lambda.php