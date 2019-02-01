#!/usr/bin/env python3


"""
Vamos criar um classe para que possamos utilizar o objeto abaixo:

my_sentence = Sentence('This is a test ')

for word in my_sentence:
    print(word)

*** Obteremos a saída:

This
is
a
test

"""


class Sentence:

    def __init__(self,sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentece = Sentence('This is a test')

for word in my_sentece:
    print(word)


#print(next(my_sentece))  # raise a StopIteration
print()


# Agora vamos criar uma funcção generator pra fazer a mesma coisa que essa classe iterator
def new_sentence(sentence):
    for word in sentence.split():
        yield word


my_sentece = new_sentence('This is a test')

for word in my_sentece:
    print(word)



#print(next(my_sentece))  # raise a StopIteration





"""Link do video original de Corey Schafer
https://www.youtube.com/watch?v=C3Z9lJXI6Qw&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=91"""