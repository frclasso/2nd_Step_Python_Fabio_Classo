#!/usr/bin/env python3


import itertools

counter = itertools.count() # start=5, step=5

#loop infinito
for x in counter:
    print(x)
#
# comenta
#ex 1
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


#ex 2
# data = [100,200,300,400]
# daily_data = list(zip(itertools.count(), data))
# print(daily_data)


# ex3 - substituindo count por range
# data = [100,200,300,400]
# daily_data = list(zip(range(10), data))  # para quando esgota o iteravel
# print(daily_data)


# comentar
# data = [100,200,300,400]
# daily_data = list(itertools.zip_longest(range(10), data))
# # completa o iteravel com None dentro do range
# print(daily_data)

# comentar/decomentar

#counter = itertools.cycle([1,2,3]) #On , Off

# repetindo valores
#counter = itertools.repeat(2, times=3)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# comente/descomente
# counter = itertools.repeat(2, times=3)
#
# #squares = map(pow, range(10), itertools.repeat(2))
#
# squares = itertools.starmap(pow, [(0,1), (1,2), (2,2)])
#
# print(list(squares))


# COMBINATION E PERMITATION
# COMBINATION A ORDEM NAO IMPORTA

letters =['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
names = ['Doe', 'Jane']


#result = itertools.combinations(letters, 2)

#result = itertools.permutations(letters, 2)  # a ordem importa

#result = itertools.product(numbers, repeat=4)  # a ordem importa

# result = itertools.combinations_with_replacement(numbers, 4)
#
#
# for item in result:
#     print(item)

#comenta/descomenta

# Iterando sobre todas as listas

# combined = itertools.chain(letters, numbers,names)
# for item in combined:
#     print(item)

#comenta/descomenta

# result = itertools.islice(range(10),1, 5, 2)  # start, stop, step
#
# for item in result:
#     print(item)


# porque isso é útil?
# with open('test.log', 'r') as f:
#     header = itertools.islice(f, 3)
#
#     for line in header:
#         print(line, end='')

#comenta/descomenta

#compress
# letters =['a', 'b', 'c', 'd']
# selectors = [True, True, False, True]
#
# result = itertools.compress(letters, selectors)
# for item in result:
#     print(item)


"""Corey Schafer
https://www.youtube.com/watch?v=Qu3dThVy6KQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=92
"""