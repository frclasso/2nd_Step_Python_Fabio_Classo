def calcula_preco(valor, **kwargs):
    taxa_porcentagem = kwargs.get('taxa_porcentagem')
    disconto = kwargs.get('desconto')


    if taxa_porcentagem:
        valor += valor * (taxa_porcentagem /100)
    if disconto:
        valor -= disconto

    return valor


preco_final = calcula_preco(1000.00, taxa_porcentagem=7)
print(preco_final)
print()

preco_final = calcula_preco(1000.00, desconto=5.0, taxa_porcentagem=7)
print(preco_final)


