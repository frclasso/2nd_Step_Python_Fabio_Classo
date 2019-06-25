# calculo IR

"""
    DESCONTO DE INSS
    Salário bruto até R$ 1.659,38 – 8% de INSS;
    Salário bruto de R$ 1.659,39 a R$ 2.765,66 – 9% de INSS;
    Salário bruto de R$ 2.765,67 a R$ 5.531,31 – 11% de INSS;
    A partir de R$ 5.531,32 – R$ 604,44 de INSS.
"""
print('-'*50)
salario_bruto = float(input('Digite seu salario: '))

if salario_bruto <= 1659.38:
    tx_inss = 0.08
    inss = salario_bruto * tx_inss
    salario = salario_bruto - inss
    print('Valor do salário com desconto de INSS: R${}'.format(salario))
    print('INSS a pagar: R${}'.format(inss))

elif salario_bruto <= 2765.66:
    tx_inss = 0.09
    inss = salario_bruto * tx_inss
    salario = salario_bruto - inss
    print('Valor do salário com desconto de INSS: R${}'.format(salario))
    print('INSS a pagar: R${:.2f}'.format(inss))
elif salario_bruto <= 5531.31:
    tx_inss = 0.11
    inss = salario_bruto * tx_inss
    salario = salario_bruto - inss
    print('Valor do salário com desconto de INSS: R${}'.format(salario))
    print('INSS a pagar: R${}'.format(inss))
else:
    inss = 604.44
    salario = salario_bruto - inss
    print('INSS a pagar: R${}'.format(inss))


print()
print('-'*50)
salario_atual = salario
print('Salario atual com devido desconto de INSS: R${:.2f} '.format(salario_atual))

"""
    FAIXAS DE DESCONTO
    1ª faixa: 7,5% para bases de R$ 1.903,99 a R$ 2.826,65;
    2ª faixa: 15% para bases de R$ 2.826,66 a R$ 3.751,05;
    3ª faixa: 22,5% para bases de R$ 3.751,06 a R$ 4.664,68;
    4ª faixa: 27,5% para bases a partir de R$ 4.664,69.
"""
#salario_atual = 5000  ## teste

isencao_primeira_faixa = salario_atual - 1903.99
#print(isencao_primeira_faixa)

if salario_atual < 1903.99:
    print('Isento')
elif salario_atual <= 2826.65:
    tx_imposto = 0.075
    ir = isencao_primeira_faixa * tx_imposto
    salario = salario_atual - ir
    print('Salario atual com desconto de 7.5%: R${:.2f}'.format(salario))
    print('Imposto devido: R${:.2f}'.format(ir))
elif salario_atual <= 3751.06:
    tx_imposto = 0.15
    ir = 733.35 * tx_imposto
    salario = salario_atual - ir
    print('Salario atual com desconto de 15%: R${}'.format(salario))
    print('Imposto devido: R${}'.format(ir))
elif salario_atual <= 4664.68:
    tx_imposto = 0.225
    ir = isencao_primeira_faixa * tx_imposto
    salario = salario_atual - ir
    print('Salario atual com desconto de 22.5%: R${}'.format(salario))
    print('Imposto devido: R${}'.format(ir))
else:
    tx_imposto = 0.275
    ir = isencao_primeira_faixa * tx_imposto
    salario = salario_atual - ir
    print('Salario atual com desconto de 27.5%: R${}'.format(salario))
    print('Imposto devido: R${}'.format(ir))
#


"""
    IMPOSTO DE RENDA RETIDO NA FONTE
    1ª faixa: R$ 142,80;
    2ª faixa: R$ 354,80;
    3ª faixa: R$ 636,13;
    4ª faixa: R$ 869,36.
"""