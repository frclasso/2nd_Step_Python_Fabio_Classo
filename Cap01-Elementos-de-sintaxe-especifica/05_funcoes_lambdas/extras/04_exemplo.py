#!/usr/bin/env python3

# No exemplo abaixo o título do nome está sendo passado como argumento padrão
def writer():
    title ='Sir'
    name = (lambda x: title + ' ' + x)
    return name


who = writer()
print(who('Arthur Ignatius Conan Doyle'))
