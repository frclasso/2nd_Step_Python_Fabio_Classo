#!/usr/bin/env python3

# ##COMENTE TODO O CODIGO ACIMA E DESCOMENTE ABAIXO
#
# # regular methods em Classes  pegam automaticamente a instância como primeiro
# # argumento por conveção chamamos de self
#
# # para pegar uma classe como primeiro argumento ao invés da instância usamos
# # os métodos de classe(class methods) atrvés do decorator @classmethod
#
#
class Employee:


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
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount): # cls = classe
        cls.raise_amt = amount

emp_1 = Employee('Fabio','Classo', 50000)
emp_2 = Employee('User', 'Test', 150000)

# run this
# print(Employee.num_of_emps)
print(Employee.raise_amount) # estao usando a variavel de classe raise_amount
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()
# coment

# run
Employee.set_raise_amt(1.05)
'''automaticamente define a classe, não é preciso passar como argumento
passamos apenas amt'''

# ou ainda poderiamos usar uma instancia de classe com o metodo de classe
# e continua funcionando
#emp_1.set_raise_amt(1.05)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# '''----------------------------------------------------------------'''
# '''COMENTE TODO O CODIGO ACIMA E DESCOMENTE ABAIXO'''
#
#
# class Employee:
#
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount
#u
#
# emp_1 = Employee('Fabio','Classo', 50000)
# emp_2 = Employee('User', 'Test', 150000)
#
#
# # instanciando objetos mais especificos
# # digamos que em sua base de dados, voce receba dados separados por '-'
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-300000'
# emp_str_3 = 'Jane-Doe-90000'
#
# # para criar um novo employee com esses dados de string
# # a primeira coisa a fazer é separar a string com o método ,spit('-')
#
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last,pay)
#
# print(new_emp_1.first,new_emp_1.last)
# print(new_emp_1.email)
# print(new_emp_1.pay)

# '''----------------------------------------------------------------'''
# '''COMENTE TODO O CODIGO ACIMA E DESCOMENTE ABAIXO'''
#
# # O que aoonteceu acima é uma maneira simples, no entanto nao queremos passar
# # a string como argumento toda vez que instanciamos um objeto
# # vamos criar um novo construtor que permite fazer isso automaticamente
#
# class Employee:
#
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount
#
#     @classmethod
#     def from_string(cls, emp_str):  # pegamos daqui first, last, pay = emp_str_1.split('-')
#         first, last, pay = emp_str_1.split('-')
#         return cls(first, last,pay)  # pegamos de Employee(first, last,pay), substituimos por cls
#
#
# # emp_1 = Employee('Fabio','Classo', 50000)
# # emp_2 = Employee('User', 'Test', 150000)
#
#
# # instanciando objetos mais especificos
# # digamos que em sua base de dados, voce receba dados separados por '-'
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-300000'
# emp_str_3 = 'Jane-Doe-90000'
#
# #
# # first, last, pay = emp_str_1.split('-')
# # new_emp_1 = Employee(first, last,pay)
#
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.first,new_emp_1.last)
# print(new_emp_1.email)
# print(new_emp_1.pay)
#

'''----------------------------------------------------------------'''
'''COMENTE TODO O CODIGO ACIMA E DESCOMENTE ABAIXO'''

"""Criando um método estático
   @staticmethods nao depende de conexão com a classe ou instância
   nao usam a classse ou instancia como primeiro parametro
   vamos criar uma função simples que retorne se um dia é ou não um dia 
   útil
"""
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):  # pegamos daqui first, last, pay = emp_str_1.split('-')
        first, last, pay = emp_str_1.split('-')
        return cls(first, last,pay)  # pegamos de Employee(first, last,pay), substituimos por cls

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_str_1 = 'John-Doe-70000'#
new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.first,new_emp_1.last)
#

# testando o staticmethod
import datetime
my_date = datetime.date(2019, 2, 7) # 07/02 sexta
print(Employee.is_workday(my_date))


'''
Corey Shafer tutorial
https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=42'''
