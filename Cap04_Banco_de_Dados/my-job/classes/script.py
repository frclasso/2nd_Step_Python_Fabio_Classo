#!/usr/bin/env python3

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print('Numero da conta:{}\nsaldo:{}'.format(self.numero, self.saldo))


minha_conta = Conta(53550, 'Fabio Classo', 1000, 1000)
print(minha_conta.saldo)
minha_conta.extrato()
minha_conta.deposita(2000)
minha_conta.extrato()
minha_conta.deposita(6000)
minha_conta.extrato()
minha_conta.saca(6000)
minha_conta.extrato()