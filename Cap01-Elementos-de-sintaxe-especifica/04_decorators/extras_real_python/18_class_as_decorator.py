#!/usr/bin/env python3


class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")


counter = Counter()
counter()
counter()
counter()

print(f'Houveram {counter.count} chamadas')
