#!/urs/bin/python


class Duck:
    def quack(self):
        print('Quaaaaaaak!')

    def walk(self):
        print("Walk like a Duck!")

    def bark(self):
        print('The duck cannot bark!')

    def fur(self):
        print('The duck has no fur')


class Dog:
    def quack(self):
        print('The dog cannot quack!')

    def walk(self):
        print("Walk like a Dog!")

    def bark(self):
        print('Woof!')

    def fur(self):
        print('The dog has brown and white fur')


def main():
    print("Donald: ")
    donald = Duck()
    in_the_forest(donald)
    in_the_pond(donald)
    print()
    print("Fido:")
    fido = Dog()
    in_the_pond(fido)
    in_the_forest(fido)


def in_the_forest(dog):
    dog.bark()
    dog.fur()


def in_the_pond(duck):
    duck.quack()
    duck.walk()
    

if __name__ == "__main__":main()