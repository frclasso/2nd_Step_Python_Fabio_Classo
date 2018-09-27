#!/usr/bin/env python3
# -*-coding:utf-8 -*-


def echo_funcname(func):
    def finterna(*args, **kwargs):
        print ("Chamando funcao: %s()" % (func.__name__))
        return func(*args, **kwargs)

    return finterna


def dobro(x):
    """ Retorna o valor dobrado.
    """
    return 2 * x


valorDobrado = echo_funcname(dobro)
print(valorDobrado(10))