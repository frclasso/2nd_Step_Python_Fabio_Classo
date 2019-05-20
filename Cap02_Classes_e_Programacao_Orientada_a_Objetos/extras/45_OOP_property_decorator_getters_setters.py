#!/usr/bin/env python3

# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
# emp_1 = Employee('John', 'Smith', 50000)
#
# # Alterando o nome para Jim
# emp_1.first = 'Jim'   # email nao altera , fullname() funciona
#
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.email)
# print(emp_1.fullname())

# """Descomente o codigo abaixo"""
#
# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     def email(self):
#         return '{}.{}@company.com'.format(self.first,self.last)
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
# emp_1 = Employee('John', 'Smith', 50000)
#
# # Alterando o nome para Jim
# emp_1.first = 'Jim'   # email nao altera , fullname() funciona
#
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.email())  # para tirar os parenteses usamos @property na função
# print(emp_1.fullname())

"""Descomente o codigo abaixo"""

# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     @property # Acessa o método como se fosse atributo
#     def email(self):
#         return '{}.{}@company.com'.format(self.first,self.last)
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
# emp_1 = Employee('John', 'Smith', 50000)
#
# # Alterando o nome para Jim
# emp_1.first = 'Jim'   # email nao altera , fullname() funciona
#
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.email)  # para tirar os parenteses usamos @property na função
# print(emp_1.fullname)

"""Descomente o codigo abaixo"""

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property # Acessa o método como se fosse atributo
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith', 50000)

# Alterando fullname para alterar os demais
emp_1.fullname = 'Peter Parker' # Error: AttributeError: can't set attribute

#del emp_1.fullname
# vamos criar um setter para fullname

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)
