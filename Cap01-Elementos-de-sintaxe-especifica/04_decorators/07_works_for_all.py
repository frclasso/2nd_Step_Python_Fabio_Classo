#!/usr/bin/env python3


def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner


@works_for_all
def data(t, d):
    return t, d


print((data(t=(1,2,3), d={"a":10, 'b':20, 'c':30})))
