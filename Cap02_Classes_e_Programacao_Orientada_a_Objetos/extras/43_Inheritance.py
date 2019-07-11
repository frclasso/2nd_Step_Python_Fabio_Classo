#!/usr/bin/env python3

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
#         Employee.num_of_emps += 1  # contador
#
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount) # ou self.raise_amount
#
# class Developer(Employee):
#     pass
#
#
#
# emp_1 = Employee('Fabio','Classo', 50000)
# emp_2 = Employee('User', 'Test', 150000)
# dev_1 = Employee('Peter', 'Parker', 20000000)
# dev_2 = Developer('Mary', 'Jane', 230000)
#
# # print(emp_1.email)
# # print(emp_2.email)
# # print(dev_1.email)
# # print(dev_2.email)
#
# # Se quiser saber o que está disponível na Classe Developer
# #print(help(Developer))
#

'''Descomente o codigo abaixo'''
# alterando os aumentos de salarios

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
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# class Developer(Employee):
#     raise_amount = 1.10
#
#
#
# emp_1 = Employee('Fabio','Classo', 50000)
# emp_2 = Employee('User', 'Test', 200000)
# dev_1 = Developer('Peter', 'Parker', 200000)
# dev_2 = Developer('Mary', 'Jane', 230000)
#
#
#
# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)
#
# print()
#
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

'''Descomente o codigo abaixo'''
# construtor de subclasse
#
# class Employee:
#
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay): # copiar para subclasse
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# class Developer(Employee):
#     raise_amount = 1.10
#
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
#
#
# dev_1 = Developer('Peter', 'Parker', 200000, 'Python')
# dev_2 = Developer('Mary', 'Jane', 230000, 'Django')
#
#
# print(dev_1.fullname())
# print(dev_1.prog_lang)
#
# print()
# print(dev_2.fullname())
# print(dev_2.prog_lang)

'''Descomente o codigo abaixo'''
# construtor de subclasse 2 - Manager

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay): # copiar para subclasse
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):  #employees => lista vazia
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):  # adiciona empregados a lista employee
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp): # remove empregados a lista employee
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):  # imprime empregados da lista employee
        for emp in self.employees:
            print('--->',emp.fullname())


dev_1 = Developer('Peter', 'Parker', 200000, 'Python')
dev_2 = Developer('Mary', 'Jane', 230000, 'Django')


mgr_1 = Manager('JJ', 'Jameson', 400000,[dev_1])

#print(mgr_1.email)
print(mgr_1.print_emp())

# Adicionando novos empregados a lista
mgr_1.add_emp(dev_2)
# print(mgr_1.print_emp())

# removendo empregados
mgr_1.remove_emp(dev_1)
#print(mgr_1.print_emp())


# Para verificar as instancias
# print(isinstance(mgr_1, Manager)) # True
# print(isinstance(mgr_1, Employee)) # True
# print(isinstance(mgr_1, Developer)) # False


# Para verificar subclasses
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))


""" Corey Schafer
https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=43"""