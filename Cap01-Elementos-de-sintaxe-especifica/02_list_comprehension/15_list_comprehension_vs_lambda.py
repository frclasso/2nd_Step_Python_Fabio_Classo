#!/usr/bin/env python3

# Criando uma lista  com quilometragens

kilometer = [39.2, 35.5, 37.3,37.8]

# Convertendo km em feet

# Utilizando list comprehension
feet = [float(3280.8399) * x for x in kilometer]
print(feet)

# Utilizando lambda
feet = map(lambda x: float(3280.8399) * x, kilometer)
print(list(feet))
