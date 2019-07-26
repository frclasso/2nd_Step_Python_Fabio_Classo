# -*- coding: UTF-8 -*-


from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

'''
 Precisamos de uma classe que monte essa corrente na ordem certa com todos os descontos necessários
 por isso a classe Calculador_de_descontos é essencial para a utilização desse design pattern
'''


# =============================================================================================
class Calculador_de_descontos(object):
    '''
      Faz o cálculo utilizando o design pattern Chain of Responsibility
    '''

    # -----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        return Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        ).calcular(orcamento)
    # -----------------------------------------------------------------------------------------

# =============================================================================================