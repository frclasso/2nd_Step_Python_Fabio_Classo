#!/usr/bin/env python3



nums = [1,2,3]
#
# for num in nums:
#     print(num)

# usando o método mágico __iter__()

#print(dir(nums)) # mesmo que dir(list)

# o que faz algo ser iterável?
# Iterator é algo que pode ser varrido por um laço/loop recordando onde está durante a iteração
# Iterator sabem tambem como obter o próximo valor __next__()

#print(next(nums)) # TypeError: 'list' object is not an iterator
# tenta rodar em background __next__()
# mas o objeti lista nao tem essa função

# vamos tentar rodar manualmente
#i_nums = nums.__iter__()  # é considerado feio chamar diretamente magic methods dessa maneira

i_nums = iter(nums) # provê o mesmo resultado

# print(i_nums)
# print(dir(i_nums))  # agora temos __iter__() e __next__()

# Agora ao chamar next(), obteremos o proximo valor da lista
#print(next(i_nums))

# raise StopIteration
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))


# Tratando a StopIteration
# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break


# Uma outra característica dos iterator é que eles só podem avançar ao ser chamado next()

# Vamos criar agora uma classe para simular o comportamento da função range

class myRange():

    def __init__(self, start, end):
        self.value = start
        self.end =end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise  StopIteration
        current = self.value
        self.value += 1
        return current

# instanciando o objeto
nums = myRange(1, 10)
# for num in nums:
#     print(num)

# Essa classe é considerada iterável pois pode ser percorrida com um laço for
# e ao mesmo tempo é um iterator por possui os métodos mágicos __iter__() e __next()__

# print('myRange...')
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# print(next(nums))  # raise Stop Iteration


# Genetators

'''Parecem funções normais mas ao invés de retornar um valor (return) um generator produz um valor
(yield).
Quando gera o valor o generator mantém os mesmos até rodar novamente e gera o próximo valor.
generator são iterator, no entanto criam automaticamente os métodos mágicos __iter__() e 
__next__()'''


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1,10)

print()
print('Generator my_range()')
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
#
#
# for num in nums:
#     print(num)

#print(next(nums))  # raise Stop Iteration


# Genertors podem ser infinitos
def infinity_gen(start):
    current = start
    while True:
        yield current
        current += 1


i = infinity_gen(1)

print(next(i))
print(next(i))

# se iniciar um laço for ... será infinito


""""
Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?
https://www.youtube.com/watch?v=jTYiNjvnHZY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=90
"""