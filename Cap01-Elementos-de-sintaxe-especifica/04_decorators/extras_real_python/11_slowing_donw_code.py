#!/usr/bin/env python3

"""The @slow_down decorator will sleep one second before it calls the decorated function"""

import functools, time


def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args,**kwargs):
        time.sleep(1)
        return func(*args,**kwargs)
    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


print(countdown(3))