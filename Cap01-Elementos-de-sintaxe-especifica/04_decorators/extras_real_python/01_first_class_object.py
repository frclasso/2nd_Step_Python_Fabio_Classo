#!/usr/bin/env python3

"""First-Class Objects
In Python, functions are first-class objects. This means that functions can be
passed around and used as arguments, just like any other object (string, int, float,
list, and so on). """


def say_hello(name):
    return f'Hello {name}'


def be_awesome(name):
    return f'Yo {name}, together we are awesomest!'


def greet_bob(func):
    return func('Bob')


print(greet_bob(say_hello))
print(greet_bob(be_awesome))

"""Here, say_hello() and be_awesome() are regular functions that expect a 
name given as a string. The greet_bob() function however, expects a function 
as its argument."""

"""Note that greet_bob(say_hello) refers to two functions, but in different ways:
 greet_bob() and say_hello. The say_hello function is named without parentheses. 
 This means that only a reference to the function is passed. The function is not 
 executed. The greet_bob() function, on the other hand, is written with 
 parentheses, so it will be called as usual.""" 