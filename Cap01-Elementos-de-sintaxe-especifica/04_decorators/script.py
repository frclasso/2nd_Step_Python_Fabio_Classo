#!/usr/bin/env python3


def timestamp(funcao_chamada):
    def inner(*args, **kwargs):
        from datetime import datetime
        print ('funcao chamada em {}'.format(datetime.now()))
        return funcao_chamada(*args, **kwargs)
    return inner


def logger(funcao_chamada):
    def inner(*args, **kwargs):
        print (funcao_chamada)
        return funcao_chamada(*args, **kwargs)
    return inner


@timestamp
@logger
def frase():
    print('Floripa Code Gurus')

frase()





"""https://www.infoq.com/br/articles/Decorators-do-Python-em-profundidade/"""