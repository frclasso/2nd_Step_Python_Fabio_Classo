#!/usr/bin/env python3

import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something
        value = func(*args, **kwargs)
        # Do something
        return value
    return wrapper_decorator


def iptu():
    pass

def ir():
    pass

def icms():
    pass

def pis():
    pass

def ipva():
    pass


# aluguel
# luz
# agua
# alimentacao
# vestuario
# educacao
# transporte_gasolina
# saude
# telefone
# gas_de_cozinha
# outros
#
# fonte https://impostometro.com.br/ImpostometroPessoal
