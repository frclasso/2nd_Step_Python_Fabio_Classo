#!/usr/bin/env python3

"""List comprehension com condição IF"""

fish_tuple = ('catfish', 'blowfish', 'clownfish','octopus')

fish_list= [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

# Utilizando endswith
fish_list2 = [fish for fish in fish_tuple if fish.endswith('fish')]
print(fish_list2)