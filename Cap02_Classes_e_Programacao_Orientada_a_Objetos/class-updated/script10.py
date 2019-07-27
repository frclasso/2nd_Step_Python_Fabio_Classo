#!/usr/bin/env python3

# Heranca multipla

"""Herança múltipla é quando uma classe pode herdar atributos e métodos de mais de uma
classe pai. Isso pode permitir que os programas reduzam a redundância, mas também
pode introduzir uma certa complexidade e ambigüidade, portanto, isso deve ser feito
pensando no projeto geral do programa.

Para mostrar como funciona a herança múltipla, vamos criar uma classe-filha Coral_reef
que herda de uma classe Coral e uma classe Sea_anemone. Podemos criar um método em cada
um e, em seguida, usar a palavra-chave pass na classe-filha Coral_reef:
"""

class Coral:
    def community(self):
        print("Coral lives in community")


class Anenome:
    def protect_clowfish(self):
        print("The anenome is protecting the clownfish.")


class CoralReef(Coral, Anenome):
    pass


"""A classe Coral tem um método chamado community () que imprime uma linha, e a classe 
Anemone possui um método chamado protect_clownfish () que imprime outra linha. 
Então nós chamamos ambas as classes na tupla de herança. Isso significa que Coral está 
herdando de duas classes pai."""

# instanciando um objeto CoralReef()
great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clowfish()


"""A saída mostra que os métodos de ambas as classes pai foram efetivamente usados ​​na 
classe filha.

A herança múltipla nos permite usar o código de mais de uma classe pai em uma classe 
filha. Se o mesmo método for definido em vários métodos pai, a classe filha usará o 
método do primeiro pai declarado em sua lista de tupla.

Embora possa ser usado com eficácia, a herança múltipla deve ser feita com cuidado para 
que nossos programas não se tornem ambíguos e difíceis para outros programadores entenderem.

"""


"""Conclusão

Este tutorial passou pela construção de classes pai e de classes filhas, substituindo 
métodos e atributos pai em classes filhas, usando a função super () e permitindo que 
classes filhas herdassem de várias classes pai.

A herança na codificação orientada a objetos pode permitir a adesão ao princípio DRY 
(não se repita) de desenvolvimento de software, permitindo que mais seja feito com menos 
código e repetição. A herança também obriga os programadores a pensar em como estão 
projetando os programas que estão criando para garantir que o código seja eficaz e claro."""


"""A programação orientada a objetos (OOP) se concentra na criação de padrões reutilizáveis 
​​de código, em contraste com a programação procedural, que se concentra em instruções 
explícitas em seqüência. Ao trabalhar em programas complexos em particular, a programação 
orientada a objetos permite reutilizar códigos e escrever códigos mais legíveis, o que, 
por sua vez, os torna mais fáceis de manter."""

