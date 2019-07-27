#!/usr/bin/env python3


class Pizza:
    """Nosso mddelo para classe do produto Pizza"""
    def __init__(self, nome, sabor, preco, tamanho, borda):
        self.nome = nome
        self.sabor = sabor
        self.preco = preco
        self.tamanho = tamanho
        self.borda = borda


class Doces(Pizza): # herança simples
    def __init__(self, nome, sabor, preco, tamanho, borda, cobertura):
        super().__init__(nome, sabor,preco,tamanho,borda)
        self.cobertura = cobertura


class especiais(Pizza):
    pass


class veganas(Pizza):
    pass


class Bebidas:
    """classe para os tipos e valores de bebidas"""
    def __init__(self, tamanho,tipo, qualidade, preco):
        self.tamanho = tamanho
        self.tipo = tipo
        self.qualidade = qualidade
        self.preco = preco

class Entrega:
    """Classe para cáculo de valor de entrega"""
    def __init__(self):
        self.__entrega_FLN = 10.00
        self.__entrega_SJ = 15.00
        self.__entrega_Palhoca = 20.00
        self.__entrega_Bigacu = 30.00
        self.__entrega_outros = 40.00


class Pagamento(Entrega):
    """Formas de pgamento"""
    def __init__(self, pagamento):
        super().__init__()
        self.pagamento = pagamento


class Pedido:
    """classe para fechamento do pedido, onde serão feitos
    todos os calculos"""
    pass


margherita = Pizza("Margherita", "margherita", "39.90",'Grande', "Catupiry")
# print(f'Sua pizza {margherita.nome}, sabor {margherita.sabor} R${margherita.preco} '
#       f'tamanho {margherita.tamanho}, com borda de {margherita.borda}')

print()

nutella = Doces("Nutella", "Avelã", "29.90", "media", "chocolate",
                "nutella derretida")

# print(f'Sua pizza doce:\n'
#       f'{nutella.nome}\n',
#       f'{nutella.sabor}\n',
#       f'{nutella.preco}\n',
#       f'{nutella.tamanho}\n',
#       f'{nutella.borda}\n',
#       f'{nutella.cobertura}')