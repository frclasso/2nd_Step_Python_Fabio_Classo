#!/usr/bin/env python3

# heranca


"""Nos inicializamos nossa variavel last_name com a string "Fish"
porque sabemos que a maioria dos peixes tera isso como seu sobrenome."""

# Parent Class
# class Fish:
#     def __init__(self, first_name, last_name="Fish"):
#         self.first_name = first_name
#         self.last_name = last_name
#
#
# # adicinando metodos
#     def swim(sef):
#         print("The Fish is swimming")
#
#     def swim_backwards(self):
#         print("The Fish can  swim in backwards")


"""Adicionamos os metodos swim () e swim_backwards () a classe Fish, 
para que cada subclasse tambem possa usar esses metodos.

"""


"""Construir uma classe pai segue a mesma metodologia que construir qualquer
 outra classe, exceto que estamos pensando sobre quais metodos as classes 
 filhas poderao usar uma vez que as criarmos."""

# Child Class

# class Trout(Fish):
#     pass

# 2-------------------------------------------

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





class Trout(Fish):
    pass

# vamos criar um objeto da classe Trout que ainda nao possui nenhum metodo proprio
terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
terry.swim()
terry.swim_backwards()
print(terry.eyelids)
print(terry.skeleton)


"""Nos criamos um objeto Trout terry que faz uso de cada um dos metodos da classe 
Fish, embora nao tenhamos definido esses metodos na classe filha Trout. Nos so 
precisavamos passar o valor de "Terry" para a variavel first_name porque todas as 
outras variaveis ​​foram inicializadas.

"""

# vamos criar outra subclasse Clownfish
class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")


print()
# vamos instanciar o objeto clownfish
casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.swim_backwards()
casey.live_with_anemone()

"""A saida mostra que o objeto Clownfish casey e capaz de usar os metodos Fish __init __ () 
e swim (), assim como seu metodo de classe filho de live_with_anemone ()."""

"""As classes filhas herdam os metodos da classe pai a que pertencem, portanto, cada classe
 filha pode fazer uso desses metodos dentro dos programas."""





"""
Referencia:
https://www.digitalocean.com/community/tutorials/
understanding-class-inheritance-in-python-3"""