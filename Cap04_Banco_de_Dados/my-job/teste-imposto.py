# -*- coding: UTF-8 -*-

'''
Created on Oct 21, 2016
@author: tca85
'''

from calculador_de_impostos import Calculador_de_impostos

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    from orcamento import Orcamento, Item
    from impostos import ICMS, ISS, ICPP, IKCV

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('Item 1', 500.0))

    imposto = Calculador_de_impostos()

    print 'ISS  %f' % (imposto.realiza_calculo(orcamento, ISS()))
    print 'ICMS %f' % (imposto.realiza_calculo(orcamento, ICMS()))
    print 'ISS com ICMS %f' % (imposto.realiza_calculo(orcamento, ISS(ICMS())))

    print 'ICPP  %f' % (imposto.realiza_calculo(orcamento, ICPP()))
    print 'IKCV  %f' % (imposto.realiza_calculo(orcamento, IKCV()))
    print 'ICPP com IKCV %f' % (imposto.realiza_calculo(orcamento, ICPP(IKCV())))
