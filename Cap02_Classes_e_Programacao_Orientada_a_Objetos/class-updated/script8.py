#!/usr/bin/env python3


# Sobreescrevendo metodos da classe Pai
"""Ate agora, examinamos a classe filha Trout que utilizou a palavra-chave pass
 para herdar todos os comportamentos Fish da classe pai e outra classe filha,
 Clownfish, que herdou todos os comportamentos da classe pai e tambem criou seu proprio
  metodo exclusivo. especifico para a classe filho. As vezes, no entanto, queremos usar
  alguns dos comportamentos da classe pai, mas nao todos eles. Quando mudamos os metodos
   de classe pai, nos os substituimos."""

"""Ao construir classes pai e filho, e importante manter o design do programa em mente 
para que a substituicao nao produza codigo desnecessario ou redundante."""

"""Diante disso, substituiremos o metodo construtor __init __ () e o metodo swim_backwards (). 
Nao precisamos modificar o metodo swim (), pois os tubaroes sao peixes que podem nadar. 
Vamos dar uma olhada nesta classe infantil:
"""

class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton='Bone', eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(sef):
        print("The Fish is swimming")

    def swim_backwards(self):
        print("The Fish can  swim in backwards")


class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
                 skeleton='Cartilage', eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The Fish can not  swim in backwards, but can sink backwards")


"""Nos substituimos os parametros inicializados no metodo __init __ (), para que a variavel
last_name seja agora igual a string "Shark", a variavel esqueleto agora e igual a string 
"cartilage", e a variavel eyelids agora esta definida para o valor booleano True. 
Cada instancia da classe tambem pode substituir esses parametros.

O metodo swim_backwards () agora imprime uma string diferente da que esta na classe pai 
Fish, porque os tubaroes nao sao capazes de nadar para tras da maneira que os peixes com ossos
 conseguem.
"""

# instanciando um objeto shark
sammy = Shark("Sammy")
print(sammy.first_name+ " "+sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)


"""A classe secundaria Shark substituiu com exito os metodos __init __ () e swim_backwards ()
da classe pai Fish, enquanto tambem herdava o metodo swim () da classe pai.

Quando houver um numero limitado de classes filhas que sao mais exclusivas do que outras, 
a substituicao dos metodos de classe pai pode ser util"""


