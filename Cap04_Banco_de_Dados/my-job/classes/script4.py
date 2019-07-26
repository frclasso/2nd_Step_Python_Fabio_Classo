#!/usr/bin/env python3


import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('data abertura:{}'.format(self.data_abertura))
        print("Transacoes:")
        for t in self.transacoes:
            print("-", t)


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
        self.historico.transacoes.append("deposito de {}".format(valor))

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))

    def extrato(self):
        print('Numero da conta:{}\nsaldo:{}'.format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))


    def transfere(self, destino, valor):
        transferencia = self.saca(valor)
        if transferencia == False:
            return False
        else:
            destino.deposita(valor)  # Erro
            self.historico.transacoes.append("transferencia de {} para conta{}".format(valor, destino.numero))
            return True




cliente = Cliente('Fabio', 'Classo', 123456789)
minha_conta = Conta(1234, cliente, 1200.00, 10000.00)

minha_conta.deposita(500)
conta2 = Conta(2222, 'Joana Gusmao',2000, 2000)
minha_conta.transfere(conta2, 200.0)
conta2.extrato()

"""https://www.caelum.com.br/apostila-python-orientacao-objetos/orientacao-a-objetos/#exerccio-primeira-classe-python"""