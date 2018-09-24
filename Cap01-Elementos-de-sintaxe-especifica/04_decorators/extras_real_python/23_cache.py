#!/usr/bin/env python3

import functools
from decorators import count_calls


def cache(func):
    """Keep a cache from previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num -1) + fibonacci(num - 2)

fibonacci(10)
print(f'Numero de chamadas da função Fibonacci {fibonacci.num_calls}.')

fibonacci(8)

"""Note that in the final call to fibonacci(8), no new calculations were needed,
 since the eighth Fibonacci number had already been calculated for fibonacci(10)."""