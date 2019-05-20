class Encapsultaion:
    def __init__(self, a, b, c):
        self.myPublic = a
        self._myProtect = b
        self.__myPrivate = c


myEncapsulation = Encapsultaion(1,2,3)
print(myEncapsulation.myPublic)
print(myEncapsulation._myProtect)
#   print(myEncapsulation.__myPrivate)
# AttributeError: 'Encapsultaion' object has no attribute '__myPrivate'
