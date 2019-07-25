# -*- coding: UTF-8 -*-

'''
Created on Oct 23, 2016
@author: tca85
'''

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    orcamento.aplica_desconto_extra()
    print orcamento.valor
    orcamento.aprova()

    orcamento.aplica_desconto_extra()
    print orcamento.valor
    orcamento.finaliza()

    # lança exceção, porque não pode aplica desconto em um orçamento finalizado
    orcamento.aplica_desconto_extra()