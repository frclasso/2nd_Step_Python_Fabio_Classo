#!/usr/bin/env python3

my_list=[1,3,6,10]
# square each term using list comprehension
print([x**2 for x in my_list])

# same thing can be done using generator expression
#print(x**2 for x in my_list)
a = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#print(next(a)) # Raise StopIteration

# print(sum(x**2 for x in my_list))
# print(max(x**2 for x in my_list))
# print(min(x**2 for x in my_list))