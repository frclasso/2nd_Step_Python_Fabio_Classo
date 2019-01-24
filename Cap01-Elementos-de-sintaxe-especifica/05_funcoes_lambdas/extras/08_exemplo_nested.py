#!/usr/bin/env python3

# nested lambdas

"""No exemplo a seguir, o lambda aparece dentro de um def e, portanto,
 pode acessar o valor que o nome x tem no escopo da função no momento
em que a função envolvente foi chamada:"""

def action(x):
    # Make anda return function, remember x
    return (lambda newx: x + newx)

ans = action(99)
print(ans)

print(ans(100))

# O mesmo código em lamda
action2 = (lambda x: (lambda newx: x + newx))
ans2 = action(99)
print(ans2)
print(ans2(100))


# Fonte
# https://www.bogotobogo.com/python/python_functions_lambda.php
