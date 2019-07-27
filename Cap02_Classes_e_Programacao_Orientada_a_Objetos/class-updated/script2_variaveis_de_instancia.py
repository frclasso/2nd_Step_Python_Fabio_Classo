#!/usr/bin/env python3

"""Variáveis ​​de nstance

Variáveis ​​de instância são propriedade de instâncias da classe. Isso significa
que, para cada objeto ou instância de uma classe, as variáveis ​​da instância são diferentes.

Ao contrário das variáveis ​​de classe, as variáveis ​​de instância são definidas nos métodos.

No exemplo da classe Shark abaixo, nome e idade são variáveis ​​de instância:

"""

class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""Quando criamos um objeto Shark, teremos que definir essas variáveis, que 
são passadas como parâmetros dentro do método construtor ou outro método.

"""

"""Como com variáveis ​​de classe, podemos chamar de forma semelhante para imprimir variáveis 
​​de instância:

"""
new_shark = Shark('Fabio', 44)
print(new_shark.name)
print(new_shark.age)

"""A saída que recebemos é composta pelos valores das variáveis ​​que inicializamos para a 
instância do objeto new_shark.

Vamos criar outro objeto da classe Shark chamado stevie:

"""

stevie = Shark("Stevie", 42)
print(stevie.name)
print(stevie.age)

"""O objeto stevie, como o objeto new_shark, passa os parâmetros específicos para essa 
instância da classe Shark para atribuir valores às variáveis ​​da instância.

Variáveis ​​de instância, pertencentes a objetos da classe, permitem que cada objeto ou 
instância tenha valores diferentes atribuídos a essas variáveis.

"""

