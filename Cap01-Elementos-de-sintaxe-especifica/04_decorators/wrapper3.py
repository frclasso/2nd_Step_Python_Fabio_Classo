#!/usr/bin/env python3
# -*-coding:utf-8-*-

import time, math

# vamos desenvolver um decorator  que calcula o tempo de execução de qq funcção
def calculate_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print ("{} - Total time taken in : {}".format(func.__name__,
                                                       end - begin))
    return wrapper

@calculate_time
def factorial(num):
    # vamos iniciar em 2 segundos
    time.sleep(2)
    print(math.factorial(num))

factorial(10)