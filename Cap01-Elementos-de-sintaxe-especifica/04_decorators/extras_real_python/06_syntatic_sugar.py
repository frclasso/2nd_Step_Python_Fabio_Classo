#!/usr/bin/env python3


def my_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()
        print("Something is happening AFTER the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


"""O Python permite que você use decoradores de maneira mais simples 
com o símbolo @, às vezes chamada de  pie sintax."""

print(say_whee())