#!/usr/bin/env python3

# Criando um dicionário
food = {'apple':'fruit', 'beetroot':'vegetable', 'cake':'dessert'}

# Updating
food['doughnut'] = 'snack'
print(food)

# Delete

del food['apple']
print(food)

food.pop('cake')
print(food)

# deletando todos os elementos
food.clear()
print(food)

# Excluindo o dicionario
del food