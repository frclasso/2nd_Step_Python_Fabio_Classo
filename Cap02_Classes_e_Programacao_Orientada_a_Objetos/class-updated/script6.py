#!/usr/bin/env python3

"""Trabalhando com mais de um objeto

As classes são úteis porque nos permitem criar muitos objetos similares baseados
no mesmo blueprint.

Para ter uma ideia de como isso funciona, vamos adicionar outro objeto Shark ao
nosso programa:"""

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

    print()
    stevie = Shark("Stevie", 40)
    stevie.swim()
    stevie.be_awsome()
    print(stevie.age)

if __name__=="__main__":
    main()

"""Nós criamos um segundo objeto Shark chamado stevie e passamos o nome "Stevie" 
para ele. Neste exemplo, usamos o método be_awesome () com sammy e o método swim () 
com stevie."""

"""A saída mostra que estamos usando dois objetos diferentes, o objeto sammy e o 
objeto stevie, ambos da classe Shark.

As classes permitem criar mais de um objeto seguindo o mesmo padrão sem criar cada 
uma delas do zero."""

"""Conclusão

Este tutorial passou por criar classes, instanciar objetos, inicializar atributos com 
o método construtor e trabalhar com mais de um objeto da mesma classe.

A programação orientada a objetos é um conceito importante a ser entendido porque 
torna a reciclagem de código mais direta, pois os objetos criados para um programa 
podem ser usados ​​em outro. Os programas orientados a objetos também contribuem para um
melhor design do programa, uma vez que programas complexos são difíceis de escrever e 
requerem um planejamento cuidadoso, e isso, por sua vez, torna menos trabalhoso manter 
o programa ao longo do tempo."""

