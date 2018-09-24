#!/usr/bin/env python3

"""The other way to use decorators on classes is to decorate the whole class.
Decorating a class does not decorate its methods. Recall that @timer is just
shorthand for TimeWaster = timer(TimeWaster)."""

from decorators import debug, timer

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


tw = TimeWaster(1000)
print()
tw.waste_time(999)