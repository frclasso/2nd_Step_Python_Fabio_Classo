#!/usr/bin/env python3

# a funcao super()

"""Com a funcao super (), você pode obter acesso a métodos herdados que foram sobrescritos
em um objeto de classe.

Quando usamos a função super (), estamos chamando um método pai para um método filho para
fazer uso dele. Por exemplo, podemos querer substituir um aspecto do método pai por uma
determinada funcionalidade, mas depois chamar o restante do método pai original para
finalizar o método."""

"""A função super () é mais comumente usada dentro do método __init __ () porque é onde você
provavelmente precisará adicionar alguma exclusividade à classe filha e então concluir a 
inicialização a partir do pai.

Para ver como isso funciona, vamos modificar nossa turma filha Trout. Como a truta é 
tipicamente peixe de água doce, vamos adicionar uma variável de água ao método __init __ ()
 e defini-la como a string "freshwater", mas manter o restante das variáveis ​​e parâmetros 
 da classe pai:"""

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
    def __init__(self, water="freshwater"):
        self.water = water
        super().__init__(self)


    def swim(sef):
        print("The Fish is swimming")

    def swim_backwards(self):
        print("The Fish can  swim in backwards")


"""Nos substituimos o método __init __ () na classe-filha Trout, fornecendo uma 
implementação diferente do __init __ () que já está definido pela sua classe-mãe Fish. 
Dentro do método __init __ () de nossa classe Trout, invocamos explicitamente o 
método __init __ () da classe Fish."""


"""Como substituímos o método, não precisamos mais passar first_name como um parâmetro 
para Trout e, se passássemos em um parâmetro, redefiniríamos "freshwater". 
Vamos, portanto, inicializar o first_name chamando a variável em nossa instância de objeto.

Agora podemos invocar as variáveis ​​inicializadas da classe pai e também usar a variável 
child exclusiva. Vamos usar isso em uma instância do Trout:"""

terry = Trout()
# inicializando first_name
terry.first_name = "Terry"

# uso do construtor da classe pai __ini__() atraves de super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)

# Construtor da classe filha __init__() sobrescrevendo o da classe pai
print(terry.water)

# usando o método swim() da classe pai
terry.swim()


"""A saída mostra que o objeto terry da classe filha Trout é capaz de fazer uso 
tanto da variável "water"  __init __ () específica da classe filha, quanto de pode chamar 
as variáveis ​​__init __ (), first_name, last_name e eyelids da classe pai  Fish.

A função interna do Python super () nos permite utilizar métodos de classe pai, 
mesmo quando sobrescrevemos certos aspectos desses métodos em nossas classes filhas."""