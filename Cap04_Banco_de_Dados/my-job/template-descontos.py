# -*- coding: UTF-8 -*-

'''
Created on Oct 18, 2016
Se o orçamento atende a regra de um desconto, o mesmo já calcula o desconto.
Caso contrário, ele passa para o "próximo" desconto, qualquer que seja esse próximo desconto,
ou seja, uma cadeia de descontos
Chain of Responsibility
Esses descontos formam como se fosse uma "corrente", ou seja, um ligado ao outro.
Daí o nome do padrão de projeto: Chain of Responsibility. A ideia do padrão é
resolver problemas como esses: de acordo com o cenário, devemos realizar alguma ação.
Ao invés de escrevermos código procedural, e deixarmos um único método descobrir
o que deve ser feito, quebramos essas responsabilidades em várias diferentes classes,
e as unimos como uma corrente.
Qual é a diferença entre uma estratégia e Chain of Responsibility?
Cada "estratégia" também possui a responsabilidade de descobrir se ela deve ser aplicada e,
caso não aplique, delegar para a próxima.
Por isso tem nas classes como Desconto_por_cinco_itens aquele "if", e por isso ela deve
saber do próximo
A intenção do Chain of Responsabilidade não é dividir a responsabilidade em fatias menores
e sim criar uma cadeia de decisão onde cada objeto representa uma responsabilidade.
@author: tca85
'''


# =============================================================================================
class Desconto_por_cinco_itens(object):

    # -----------------------------------------------------------------------------------------
    def __init__(self, proximo_desconto):
        self._proximo_desconto = proximo_desconto

    # -----------------------------------------------------------------------------------------
    def calcular(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self._proximo_desconto.calcular(orcamento)
    # -----------------------------------------------------------------------------------------


# =============================================================================================
class Desconto_por_mais_de_quinhentos_reais(object):

    # -----------------------------------------------------------------------------------------
    def __init__(self, proximo_desconto):
        self._proximo_desconto = proximo_desconto

    # -----------------------------------------------------------------------------------------
    def calcular(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self._proximo_desconto.calcular(orcamento)
    # -----------------------------------------------------------------------------------------


# =============================================================================================
'''
 Repare que essa é a última condição de descontos da cadeia. Ela não precisa ter
 o método construtor recebendo o próximo desconto, por isso retorna zero.
'''


class Sem_desconto(object):
    # -----------------------------------------------------------------------------------------
    def calcular(self, orcamento):
        return 0
    # -----------------------------------------------------------------------------------------
# =============================================================================================