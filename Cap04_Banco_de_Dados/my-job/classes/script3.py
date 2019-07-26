#!/usr/bin/env python3


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


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

cliente = Cliente('Fabio', 'Classo', 123456789)
minha_conta = Conta(1234, cliente, 1200.00, 10000.00)


print(minha_conta.titular)
print(minha_conta.titular.nome)
print()
print(type(minha_conta.numero))
print(type(minha_conta.saldo))
print(type(minha_conta.titular))