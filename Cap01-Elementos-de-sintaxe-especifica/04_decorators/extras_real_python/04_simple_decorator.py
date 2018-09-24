#!/usr/bin/env python3


def my_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()
        print("Something is happening AFTER the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

print(say_whee())

"""The so-called decoration happens at the following line:
    say_whee = my_decorator(say_whee)
    
    In effect, the name say_whee now points to the wrapper() inner function. 
    Remember that you return wrapper as a function when you call 
    my_decorator(say_whee)
    However, wrapper() has a reference to the original say_whee() as 
    func, and calls that function between the two calls to print().

    Put simply: decorators wrap a function, modifying its behavior.
"""