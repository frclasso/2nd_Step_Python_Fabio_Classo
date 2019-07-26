from abc import ABCMeta, abstractmethod

class AbstractClassExample(metaclass=ABCMeta):

    @abstractmethod
    def do_something(self):
        print('Some implementations')

class AnotherSubClass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        print('The enrichment from AnotherSubClass')


x = AnotherSubClass()
x.do_something()
