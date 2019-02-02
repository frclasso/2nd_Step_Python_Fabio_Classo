#!/usr/bin/env python3

# Classes e instances

# definindo uma classe
# class Employee:
#     pass

# instanciando a classe, criando objetos
# emp_1 = Employee()
# emp_2 = Employee()


# verificando a existencia dos objetos
# print(emp_1)
# print(emp_2)

# passando alguns atributos aos objetos criados
# emp_1.first = 'Fabio'
# emp_1.last = 'Classo'
# emp_1.email = 'fabio.classo@company.com'
# emp_1.pay = 50000


# emp_2.first = 'User'
# emp_2.last = 'Test'
# emp_2.email = 'user.test@company.com'
# emp_2.pay = 150000

# print(emp_1.email)
# print(emp_2.email)

# COMENTE O CODIGO ACIMA

class Employee:
    # construtor de classe
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    # descomentar a funcao abaixo
    def fullname(self):
        return '{} {}'.format(self.first,self.last)



# instanciando
emp_1 = Employee('Fabio','Classo', 50000)
emp_2 = Employee('User', 'Test', 150000)

# emp_1 ==> é passado para self, e o método construtor __init__ roda automaticamente

print(emp_1.email)
print(emp_2.email)
print('{} {}'.format(emp_1.first,emp_1.last)) # comente para chamar fullname()

print(emp_1.fullname()) # com parenteses, porque é um método, nao um atributo

# É possível acessar a função  através do nome da classe
Employee.fullname(emp_1)


'''
Corey Shafer tutorial
https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=40'''