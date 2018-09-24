#!/usr/bin/env python3

# wrapper() is a regular Python function

from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            print("Hush, the neighbors are asleep")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)

print(say_whee())