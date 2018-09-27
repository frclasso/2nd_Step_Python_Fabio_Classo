#!/usr/bin/env python3


class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='Quack!')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type='velociraptor',name='veronica', sound='hello'))
    print_animal(Animal())  # USA VALOR DEFAULT DO CONSTRUTOR , LINHAS 6,7 e 8.


if __name__=="__main__":main()