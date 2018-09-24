#!/usr/bin/env python3

"""There are two different ways you can use decorators on classes.
The first one is very close to what you have already done with functions:
you can decorate the methods of a class. This was one of the motivations
for introducing decorators back in the day."""

from decorators import debug, timer


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])



tw = TimeWaster(1000)
print()
tw.waste_time(999)