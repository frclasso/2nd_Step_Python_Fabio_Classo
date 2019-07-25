# -*- coding: UTF-8 -*-

'''
Created on Oct 17, 2016
https://cursos.alura.com.br/course/design-patterns-python
Design Patterns Python I: Boas práticas de programação
@author: tca85
'''

'''
Nossos orçamentos podem ter diferentes estados durante o seu ciclo de vida. Um orçamento nasce 
"Em aprovação" e pode virar "Aprovado" ou "Reprovado". Ao final de todo o processo, deverá ser "Finalizado".
Dependendo do estado que o orçamento se encontra, algumas ações podem ser diferentes. 
Por exemplo, podemos adicionar um desconto extra ao orçamento
Em implementações mais procedurais, desenvolvedores geralmente optam por representar o estado 
do objeto por meio de constantes e um método para aplicar os descontos com vários ifs
1) Geralmente outros comportamentos dessa classe também variam de acordo com o estado do objeto;
2) A cada novo estado, um novo if deve ser acrescentado em todos os métodos do objeto
Qual a solução?
Para eliminarmos esses vários ifs, precisamos primeiro separar cada ação de acordo com o estado 
em uma classe diferente.
Todas essas classes são possíveis estados de um orçamento, o que nos leva a crer que poderíamos ter 
um método comum para todas elas, por isso criamos uma classe abstrata com métodos abstratos
A principal situação que faz emergir o Design Pattern State é a necessidade de implementação de 
uma máquina de estados. Geralmente, o controle das possíveis transições entre estados são várias, 
também são complexas, fazendo com que a implementação não seja simples. O State auxilia a manter 
o controle dos estados simples e organizados, através da criação de classes que representem cada 
estado e sabendo controlar as transições entre eles.
'''

from abc import ABCMeta, abstractmethod


# =============================================================================================
class Estado_de_um_orcamento(object):
    __metaclass__ = ABCMeta

    # -----------------------------------------------------------------------------------------
    def __init__(self):
        self.desconto_aplicado = False

    # -----------------------------------------------------------------------------------------
    @abstractmethod
    def aplica_desconto_extra(self, orcamento): pass

    # -----------------------------------------------------------------------------------------
    @abstractmethod
    def aprova(self, orcamento): pass

    # -----------------------------------------------------------------------------------------
    @abstractmethod
    def reprova(self, orcamento): pass

    # -----------------------------------------------------------------------------------------
    @abstractmethod
    def finaliza(self, orcamento): pass
    # -----------------------------------------------------------------------------------------


# =============================================================================================
class Em_aprovacao(Estado_de_um_orcamento):

    # -----------------------------------------------------------------------------------------
    def aplica_desconto_extra(self, orcamento):
        if (not self.desconto_aplicado):
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')

    # -----------------------------------------------------------------------------------------
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    # -----------------------------------------------------------------------------------------
    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    # -----------------------------------------------------------------------------------------
    def finaliza(self, orcamento):
        raise Exception('Orcamento em aprovação não podem ir para finalizado diretamente')
    # -----------------------------------------------------------------------------------------


# =============================================================================================

class Aprovado(Estado_de_um_orcamento):

    # -----------------------------------------------------------------------------------------
    def aplica_desconto_extra(self, orcamento):
        if (not self.desconto_aplicado):
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')

    # -----------------------------------------------------------------------------------------
    def aprova(self, orcamento):
        raise Exception('Orçamento já está em estado de aprovação')

    # -----------------------------------------------------------------------------------------
    def reprova(self, orcamento):
        raise Exception('Orçamento está em estado de aprovação e não pode ser reprovado')

    # -----------------------------------------------------------------------------------------
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()
    # -----------------------------------------------------------------------------------------


# =============================================================================================

class Reprovado(Estado_de_um_orcamento):

    # -----------------------------------------------------------------------------------------
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    # -----------------------------------------------------------------------------------------
    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser aprovado')

    # -----------------------------------------------------------------------------------------
    def reprova(self, orcamento):
        raise Exception('Orçamento já está em estado de reprovação')

    # -----------------------------------------------------------------------------------------
    def finaliza(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser finalizado')
    # -----------------------------------------------------------------------------------------


# =============================================================================================

class Finalizado(Estado_de_um_orcamento):

    # -----------------------------------------------------------------------------------------
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos finalizados não recebem desconto extra')

    # -----------------------------------------------------------------------------------------
    def aprova(self, orcamento):
        raise Exception('Orçamento finalizado já foi aprovado')

    # -----------------------------------------------------------------------------------------
    def reprova(self, orcamento):
        raise Exception('Orçamento já finalizado não pode ser reprovado')

    # -----------------------------------------------------------------------------------------
    def finaliza(self, orcamento):
        raise Exception('Orçamento já foi finalizado')
    # -----------------------------------------------------------------------------------------


# =============================================================================================
class Orcamento(object):

    # -----------------------------------------------------------------------------------------
    def __init__(self):
        self.__itens = []

        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    # -----------------------------------------------------------------------------------------
    def aprova(self):
        self.estado_atual.aprova(self)

    # -----------------------------------------------------------------------------------------
    def reprova(self):
        self.estado_atual.reprova(self)

    # -----------------------------------------------------------------------------------------
    def finaliza(self):
        self.estado_atual.finaliza(self)

    # -----------------------------------------------------------------------------------------
    def adiciona_item(self, item):
        self.__itens.append(item)

    # -----------------------------------------------------------------------------------------
    @property
    def total_itens(self):
        return len(self.__itens)
        # -----------------------------------------------------------------------------------------

    '''
     Retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
    '''

    def obter_itens(self):
        return tuple(self.__itens)
        # -----------------------------------------------------------------------------------------

    '''
     Criamos o atributo valor como property ou seja seu acesso é apenas leitura. Isso garante 
     que o valor recebido pelo construtor não seja alterado depois do orçamento criado

     Quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
    '''

    @property
    def valor(self):
        total = 0.0

        for item in self.__itens:
            total += item.valor

        return total - self.__desconto_extra

    # -----------------------------------------------------------------------------------------
    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    # -----------------------------------------------------------------------------------------
    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)
    # -----------------------------------------------------------------------------------------


# =============================================================================================

# um item criado não pode ser alterado, suas propriedades são somente leitura
class Item(object):

    # -----------------------------------------------------------------------------------------
    def __init__(self, nome, valor):
        # atributos 'privados'
        self.__nome = nome
        self.__valor = valor

    # -----------------------------------------------------------------------------------------
    @property
    def nome(self):
        return self.__nome
        # -----------------------------------------------------------------------------------------

    @property
    def valor(self):
        return self.__valor
    # -----------------------------------------------------------------------------------------

# =============================================================================================