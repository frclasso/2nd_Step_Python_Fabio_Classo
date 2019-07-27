#!/usr/bin/env python3


"""O método construtor

O método construtor é usado para inicializar dados. É executado assim que um objeto
de uma classe é instanciado. Também conhecido como o método __init__, será a primeira
definição de uma classe e se parece com isso:
"""

# class Shark:
#
#     def __init__(self):
#         print("This is the constructor method")
#
#     def swim(self):
#         print("The  shark is swimming")
#
#     def be_awsome(self):
#         print("The shark is being awesome.")
#
# sammy = Shark()
# sammy.swim()
# sammy.be_awsome()

"""Se você adicionou o método __init__ acima à classe Shark no programa acima, o programa 
produziria o seguinte sem modificar nada dentro da instanciação sammy:"""

# output
"""This is the constructor method
The  shark is swimming
The shark is being awesome."""



"""
    Isso ocorre porque o método construtor é inicializado automaticamente. Você deve usar este 
método para realizar qualquer inicialização que você gostaria de fazer com seus objetos de classe.

Em vez de usar o método do construtor acima, vamos criar um que use uma variável de nome que 
possamos usar para atribuir nomes a objetos. Vamos passar o nome como parâmetro e definir self.name
 igual ao nome:
"""

# class Shark:
#
#     def __init__(self, name):
#         self.name = name
#
#
#     def swim(self):
#         #referenciando a variavel name
#         print(self.name + "is swimming")
#
#     def be_awsome(self):
#         print(self.name + "is being awesome.")


"""Finalmente, podemos definir o nome do sammy do objeto Shark como igual a "Sammy", passando-o 
como um parâmetro da classe Shark:"""

# def main():
#     sammy = Shark("Sammy")
#     sammy.swim()
#     sammy.be_awsome()
#
# if __name__=="__main__":
#     main()


"""Vemos que o nome que passamos para o objeto está sendo impresso. Definimos o método __init__ 
com o nome do parâmetro (juntamente com a palavra-chave self) e definimos uma variável dentro 
do método.

Como o método construtor é automaticamente inicializado, não precisamos chamá-lo explicitamente, 
apenas passar os argumentos entre parênteses após o nome da classe quando criamos uma nova 
instância da classe.

Se quiséssemos adicionar outro parâmetro, como a idade, poderíamos fazer isso passando-o para o 
método __init__:"""

class Shark:

    def __init__(self, name, age):
        self.name = name
        self.age = age



    def swim(self):
        #referenciando a variavel name
        print(self.name + "is swimming")

    def be_awsome(self):
        print(self.name + "is being awesome.")

def main():
    sammy = Shark("Sammy", 34)
    sammy.swim()
    sammy.be_awsome()

if __name__=="__main__":
    main()