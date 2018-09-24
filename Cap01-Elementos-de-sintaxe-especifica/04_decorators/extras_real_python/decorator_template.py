#!/usr/bin/env python3

import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something
        value = func(*args, **kwargs)
        # Do something
        return value
    return wrapper_decorator

# This formula is a good boilerplate template for building more complex decorators.
