class myClass:
    """This is my second class."""
    a = 10

    def func(self):
        print('Hello.')


# criando um objeto myClass
ob = myClass()

# output <function myClass.func at 0x7f676aa47400>
print(myClass.func)
print(id(myClass.func))
# output <bound method myClass.func of <__main__.myClass object at 0x7f676bf93630>>
print(ob.func)
print(id(ob.func))
# chamando a funcao func()
# output 'Hello'
ob.func()