class C:
    def __init__(self):
        print('Construtor de C')
        self.x = 1


class D:
    def __init__(self):
        print('Construtor de D')
        C.__init__(self)
        self.y = 2


d = D()
# output: Construtor de D
# output: Construtor de C
print(d.x) # 1
print(d.y) # 2