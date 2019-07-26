from abc import ABCMeta

class AbstractClassExample(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42

class DoMult42(AbstractClassExample):
    def do_something(self):
        return self.value * 42

x = DoAdd42(10)
y = DoMult42(10)
print(x.do_something())
print(y.do_something())
