#!/usr/bin/env python3


class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result


def PowTowGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


a = PowTowGen(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#print(next(a)) # Raise StopIteration