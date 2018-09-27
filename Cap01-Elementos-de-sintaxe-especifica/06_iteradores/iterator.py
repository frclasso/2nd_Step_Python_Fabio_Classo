#!/usr/bin/env python3

# Definindo uma lista
my_list =[4,7,0,3]

# Obtendo um iterador usando iter()
my_iter = iter(my_list)

# Utilizando next() para iterar
print(next(my_iter))  # imprime 4
print(next(my_iter))  # imprime 7

# next(obj) é o mesmo que obj.__next__()
print(my_iter.__next__()) # imprime 0
print(my_iter.__next__()) # imprime 3

# Raise StopIteration
#next(my_iter)

# Uma maneira mais simples...
# for element in my_list:
#     print(element)
