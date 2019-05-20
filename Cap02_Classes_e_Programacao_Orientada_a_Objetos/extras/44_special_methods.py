#!/usr/bin/env python3


# __repr__ Representação não ambígua do objeto, muito usada em Debugging e logging

# __str__ é uma representação mais legível do objeto


# class Employee:
#
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
#     # desconmente o codigo abaixo -- (1)
#     def __repr__(self):
#         """Vamos recriar o mesmo objeto"""
#         return "Employee('{}', '{}','{})".format(self.first, self.last,self.pay)
#
#     # desconmente o codigo abaixo -- (2)
#     def __str__(self):
#         return '{} - {}'.format(self.fullname(), self.email)
#
#
#
# emp_1 = Employee('Fabio','Classo', 50000)
# emp_2 = Employee('User', 'Test', 150000)

# imprime o endereço de memoria
#print(emp_1)
# 1) - print(emp_1) depois de __repr__
# 2) - print(emp_1) depois de __str__


# Podemos ainda acessar os valores de __repr__ e __str__
#print(repr(emp_1)) # ou print(emp_1.__repr__))
#print(str(emp_1)) # ou print(emp_1.__str__))


""" Comente o codigo adima e Desconmente o codigo abaixo"""

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

    def __repr__(self):
        """Vamos recriar o mesmo objeto"""
        return "Employee('{}', '{}','{})".format(self.first, self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # 1
    def __add__(self, other):
        return self.pay + other.pay

    # 2
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Fabio','Classo',50000)
emp_2 = Employee('User', 'Test', 150000)



# explicando metodos mágicos - 1
# print(1 + 2)
# # eh o mesmo que
# print(int.__add__(1,2))
#
# print('a'+ 'b')
# print(str.__add__('a', 'b'))

# 1
#print(emp_1 + emp_2)


# explicando metodos mágicos - 2
# print(len('test'))
# print('test'.__len__())

# 2
print(len(emp_1))

"""Corey Schafer
https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=44"""