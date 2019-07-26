#!/usr/bin/env python3

class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
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


    def transfere(self, destino, valor):
        transferencia = self.saca(valor)
        if transferencia == False:
            return False
        else:
            destino.deposita(valor)  # Erro
            return True

minha_conta = Conta(54550, 'Fabio', 1000,500)
minha_conta.transfere(5444, 300.0)
minha_conta.extrato()
