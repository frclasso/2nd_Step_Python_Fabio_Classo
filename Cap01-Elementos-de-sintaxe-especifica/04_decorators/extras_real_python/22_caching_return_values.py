#!/usr/bin/env python3

from decorators import count_calls


@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num -1) + fibonacci(num - 2)

fibonacci(10)
print(f'Numero de chamadas da função Fibonacci {fibonacci.num_calls}.')