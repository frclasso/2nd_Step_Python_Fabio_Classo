#!/usr/bin/env python3

"""Trabalhando com variáveis ​​de classe e instância juntas

Variáveis ​​de classe e variáveis ​​de instância costumam ser utilizadas ao mesmo tempo,
portanto, vamos ver um exemplo disso usando a classe Shark que criamos. Os comentários
no programa descrevem cada etapa do processo."""


class Shark:

    # variaveis de classe
    animal_type = 'fish'
    location = 'ocean'

    # metodo construtor com as variaves de instancia name e age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # metodo para definir  a variavel followers
    def set_follwers(self, followers):
        print("This user has  " + str(followers) + " followers")


def main():
    sammy = Shark('Sammy', 32)
    print(sammy.name)
    print(sammy.age)
    print(sammy.location)
    print()

    # segundo objeto
    stevie = Shark('Stevie',  34)
    print(stevie.name)
    print(stevie.age)
    print(stevie.location)
    print(stevie.animal_type)

if __name__=="__main__":
    main()


"""Aqui, usamos as variáveis ​​class e instance em dois objetos da classe Shark, sammy
 e stevie."""


"""
Conclusão

Na programação orientada a objetos, as variáveis ​​no nível da classe são referidas como 
variáveis ​​de classe, enquanto as variáveis ​​no nível do objeto são chamadas de variáveis 
​​de instância.

Essa diferenciação nos permite usar variáveis ​​de classe para inicializar objetos com um 
valor específico atribuído a variáveis ​​e usar variáveis ​​diferentes para cada objeto com 
variáveis ​​de instância.

O uso de variáveis ​​específicas de classe e de instância pode garantir que nosso código 
siga o princípio DRY para reduzir a repetição no código."""


"""referencias:
https://www.digitalocean.com/community/tutorials/
understanding-class-and-instance-variables-in-python-3"""