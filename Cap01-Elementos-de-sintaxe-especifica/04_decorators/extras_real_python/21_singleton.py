#!/usr/bin/env python3

"""A singleton is a class with only one instance.
There are several singletons in Python that you use frequently,
including None, True, and False."""

import functools

def singleton(cls):
    """Make a class Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass


first_one = TheOne()
second_one = TheOne()

print(id(first_one))
print(id(second_one))