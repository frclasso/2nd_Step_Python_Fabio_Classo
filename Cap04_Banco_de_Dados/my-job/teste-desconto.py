# -*- coding: UTF-8 -*-

'''
Created on Oct 23, 2016
@author: tca85
'''

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    from orcamento import Orcamento, Item
    from calculador_de_descontos import Calculador_de_descontos

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print 'Desconto calculado : %s' % (desconto)