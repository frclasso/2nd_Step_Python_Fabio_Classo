#!/usr/bin/env python3

# sorted
# sorted(iterable[, key][, reverse])

death = [
    ('John', 'Lennon', 40),
    ('James', 'Dean', 24),
    ('Jimi', 'Hendrix', 27),
    ('George', 'Gershwin', 38),
]

s = sorted(death, key=lambda age: age[2])
print(s)



# Fonte
# https://www.bogotobogo.com/python/python_functions_lambda.php
