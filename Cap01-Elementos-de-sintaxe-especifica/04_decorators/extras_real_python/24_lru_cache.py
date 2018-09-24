#!/usr/bin/env pthon3

import functools


@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating Fibonacci ({num})")
    if num < 2:
        return num
    else:
        return fibonacci(num -1) + fibonacci(num - 2)


fibonacci(10)

"""The maxsize parameter specifies how many recent calls are cached. 
The default value is 128, but you can specify maxsize=None to cache all 
function calls. However, be aware that this can cause memory problems if 
you are caching many large objects."""

print('*'* 30)
fibonacci(5)
print('*'* 30)
fibonacci(8)
print('*'* 30)
fibonacci(5)
print(fibonacci.cache_info())