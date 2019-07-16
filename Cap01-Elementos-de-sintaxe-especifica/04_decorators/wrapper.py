#!/usr/bin/env python3

def decorator(funcao):
    def wrapper():
        print ("Estou antes da funcao passada como argumento")
        funcao()
        print ("Estou localizado depois da funcao passada como argumento")
    return wrapper



def outra_funcao():
    print("Floripa Code Gurus curso Python módulo 2 - 2019.")

d = decorator(outra_funcao)
d()

print('-'*80)
