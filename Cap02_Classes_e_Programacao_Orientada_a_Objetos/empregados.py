#!/usr/bin/env python3
# -*-coding:utf-8 -*-


class Employee:
    'Classe Base para todos os empregados/Commom base class for all employees.'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(f"Total de empregados: {Employee.empCount}")

    def displayEmployee(self):
        print("Nome: ", self.name, "-", "Salario: R$", self.salary)

#This would create the first object of Eployee class
emp1 = Employee('Zara', 2000)
#This would create the second object of Eployee class
emp2 = Employee('Manni', 5000)

# Acessing Attributes
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee {}".format(Employee.empCount))

# Adicionando, modificando e deletando atributos
# emp1.salary = 3000  # altera o valor do salario
# emp1.name = 'Joseph' # altera o nome do empregado 1
#emp1.displayEmployee()
#del emp1.salary

# Verificar atributos dos objetos
# print(hasattr(emp1, 'salary')) # Retorna True se o atributo 'salary' existir
# print(getattr(emp1, 'salary')) # Retorna o valor  do atributo 'salary'
# setattr(emp1, 'salary', 4000) # Define o novo valor
# print(getattr(emp1, 'salary'))
# delattr(emp1,'salary')  # Deleta o atributo 'salary'
# print(hasattr(emp1, 'salary'))

# Verificar atributos de classe
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Emplyee.__module: ", Employee.__module__)
print("Employee.__bases__: ", Employee.__bases__)
print("Employee.__dict__: ", Employee.__dict__)

