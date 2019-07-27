#!/usr/bin/env python3

# Construindo classes e definindo objetos


"""Python é uma linguagem de programação orientada a objetos. A programação
orientada a objetos (OOP) se concentra na criação de padrões reutilizáveis ​​de
código, em contraste com a programação procedural, que se concentra em instruções
explícitas em seqüência. Ao trabalhar em programas complexos em particular, a
programação orientada a objetos permite reutilizar códigos e escrever códigos mais
legíveis, o que, por sua vez, os torna mais fáceis de manter.

"""

"""Um dos conceitos mais importantes na programação orientada a objetos é a distinção 
entre classes e objetos, que são definidos da seguinte maneira:"""

"""Class - Um blueprint criado por um programador para um objeto. Isso define um 
conjunto de atributos que caracterizarão qualquer objeto que seja instanciado 
por essa classe.
"""

"""Objeto - uma instância de uma classe. Esta é a versão realizada da classe, onde a 
classe é manifestada no programa."""


"""Estes são usados ​​para criar padrões (no caso de classes) e, em seguida, fazer uso 
dos padrões (no caso de objetos).
Neste tutorial, vamos criar classes, instanciar objetos, inicializar atributos com o 
método construtor e trabalhar com mais de um objeto da mesma classe.
"""

"""Classes

Classes são como um blueprint ou um protótipo que você pode definir para usar para 
criar objetos.

Definimos classes usando a palavra-chave class, semelhante a como definimos funções 
usando a palavra-chave def.

Vamos definir uma classe chamada Shark que tenha duas funções associadas a ela, uma 
para 'swimming' e    outra para ser 'be_awesome' :"""

class Shark:
    def swim(self):
        print("The  shark is swimming")

    def be_awsome(self):
        print("The shark is being awesome.")

"""Como essas funções são recuadas na classe Shark, elas são chamadas de métodos. 
Os métodos são um tipo especial de função que são definidos dentro de uma classe.

O argumento para essas funções é a palavra self, que é uma referência a objetos que 
são feitos com base nessa classe. Para referenciar instâncias (ou objetos) da classe, 
o self sempre será o primeiro parâmetro, mas não precisa ser o único.

Definir essa classe não criou nenhum objeto Shark, apenas o padrão para um objeto Shark 
que podemos definir mais tarde. Ou seja, se você executar o programa acima neste estágio, 
nada será retornado.

Criar a classe Shark acima nos forneceu um blueprint para um objeto."""

"""Objetos

Um objeto é uma instância de uma classe. Podemos pegar a classe Shark definida acima e 
usá-la para criar um objeto ou uma instância dela.

Vamos fazer um objeto Shark chamado sammy:"""

sammy = Shark()

"""Aqui, inicializamos o objeto sammy como uma instância da classe, definindo-o como 
igual a Shark ().

Agora, vamos usar os dois métodos com o sammy do objeto Shark:

"""

sammy.swim()
sammy.be_awsome()

"""O sammy do objeto Shark está usando os dois métodos swim () e be_awesome (). Nós os 
chamamos usando o operador ponto (.), Que é usado para referenciar um atributo do objeto. 
Nesse caso, o atributo é um método e é chamado com parênteses, como você também chamaria 
com uma função.

Como a palavra-chave self era um parâmetro dos métodos definidos na classe Shark, o 
objeto sammy é passado para os métodos. O parâmetro self garante que os métodos tenham 
uma maneira de se referir aos atributos do objeto.

Quando chamamos os métodos, no entanto, nada é passado dentro dos parênteses, o objeto sammy 
está sendo passado automaticamente com o operador ponto."""




"""Referecia:https://www.digitalocean.com/community/tutorials/
how-to-construct-classes-and-define-objects-in-python-3#the-constructor-method"""