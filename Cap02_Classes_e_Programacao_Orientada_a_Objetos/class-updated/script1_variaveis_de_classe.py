#!/usr/bin/env python3


"""A programação orientada a objetos permite que variáveis ​​sejam usadas no nível da
classe ou no nível da instância. As variáveis ​​são essencialmente símbolos que
representam um valor que você está usando em um programa.

No nível da classe, as variáveis ​​são chamadas de variáveis ​​de classe, enquanto as
variáveis ​​no nível da instância são chamadas de variáveis ​​de instância.

Quando esperamos que as variáveis ​​sejam consistentes entre instâncias ou quando
gostaríamos de inicializar uma variável, podemos definir essa variável no nível de
classe. Quando antecipamos que as variáveis ​​serão alteradas de maneira significativa
nas instâncias, podemos defini-las no nível da instância.

Um dos princípios do desenvolvimento de software é o princípio DRY, que não se repete.
Este princípio é voltado para limitar a repetição dentro do código, e a programação
orientada a objetos adere ao princípio DRY, pois reduz a redundância.

"""



"""Variáveis ​​de Classe

Variáveis ​​de classe são definidas dentro da construção da classe. Como eles pertencem 
à própria classe, as variáveis ​​de classe são compartilhadas por todas as instâncias da classe. Portanto, eles geralmente terão o mesmo valor para cada instância, a menos que você esteja usando a variável de classe para inicializar uma variável.

Definidas fora de todos os métodos, as variáveis ​​de classe são, por convenção, 
normalmente colocadas logo abaixo do cabeçalho da classe e antes do método construtor 
e de outros métodos."""

# exemplo de variavel de classe
# class Shark:
#     animal_type = 'fish'

"""Podemos criar uma instância da classe Shark (vamos chamá-la de new_shark) e imprimir a 
variável usando a notação de ponto:"""

# new_shark = Shark()
# print(new_shark.animal_type)


"""Vamos adicionar mais algumas variáveis de classe"""
class Shark:
    animal_type = 'fish'
    location = 'ocean'
    followers = 5

new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)

"""Assim como com qualquer outra variável, as variáveis ​​de classe podem consistir 
em qualquer tipo de dados disponível para nós no Python. Neste programa temos 
strings e um inteiro."""


"""A instância de new_shark é capaz de acessar todas as variáveis ​​de classe e 
imprimi-las quando executamos o programa.

Variáveis ​​de classe nos permitem definir variáveis ​​ao construir a classe. Essas 
variáveis ​​e seus valores associados são acessíveis a cada instância da classe."""


