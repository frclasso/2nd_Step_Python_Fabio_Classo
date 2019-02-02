#!/usr/bin/env python3

# variaveis de classe

#
# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * 1.04)
#
#
# # instanciando
# emp_1 = Employee('Fabio','Classo', 50000)
# emp_2 = Employee('User', 'Test', 150000)
#
#
# # Aumento de salario
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#

# # COMENTE TODO O CODIGO ACIMA E DESCOMENTE ABAIXO
#
#
# class Employee:
#
#     raise_amount = 1.04  # variavel de classe
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
#     def apply_raise(self):
#         #self.pay = int(self.pay * raise_amount)  # Error: NameError: name 'raise_amount' is not defined
#         self.pay = int(self.pay * Employee.raise_amount) # ou self.raise_amount
#
#
# # instanciando
# emp_1 = Employee('Fabio','Classo', 50000)
# emp_2 = Employee('User', 'Test', 150000)
#
#
# # Aumento de salario
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print()
#
# # Acessando a variavel raise_amount
# print(Employee.raise_amount) # Diretamente via nome da classe
# print(emp_1.raise_amount) # através da instância de classe
# print(emp_2.raise_amount)
# print()
#
# # um pequeno truque para entender o que está acontecendo aqui é imprimir o namespace/escopo
# print(emp_1.__dict__)
# print()
#
# #print(Employee.__dict__)  # raise_amount
# print()
#


#Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.05  # cria/altera um atributo de instancia
# print(emp_1.__dict__)
#
# print(Employee.raise_amount) # Diretamente via nome da classe
# print(emp_1.raise_amount) # através da instância de classe
# print(emp_2.raise_amount)
#

##COMENTE TODO O CODIGO ACIMA E DESCOMENTE ABAIXO


class Employee:

    # adcionando outra variavel
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1  # contador


    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        #self.pay = int(self.pay * raise_amount)  # Error: NameError: name 'raise_amount' is not defined
        self.pay = int(self.pay * Employee.raise_amount) # ou self.raise_amount


# 2) imprimindo numero de empregados Employee.num_of_emps, antes de instanciar
print(Employee.num_of_emps)

emp_1 = Employee('Fabio','Classo', 50000)
emp_2 = Employee('User', 'Test', 150000)


# 1) imprimindo numero de empregados Employee.num_of_emps
print(Employee.num_of_emps)




'''
Corey Shafer tutorial
https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=41'''