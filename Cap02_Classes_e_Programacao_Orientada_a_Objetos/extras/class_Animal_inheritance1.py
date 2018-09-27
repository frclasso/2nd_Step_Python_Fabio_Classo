#!/urs/bin/python


class Animal():
    def talk(self): print('I have something to say!')

    def walk(self): print("Hey! I'm walking here.") # METODO GLOBAL

    def clothes(self):print("I have nice clothes.")


class Duck(Animal):
    def quack(self):
        print('Quaaaaaaak!')

    def walk(self): # METODO LOCAL SOBREESCREVE METODO GLOBAL
        print("Walk like a Duck!")


class Dog(Animal):
    def clothes(self):
        print('I have brown and white fur.')


def main():
    print("Donald: ")
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    print()
    print("Fido:")
    fido = Dog()
    fido.walk()
    fido.talk()
    fido.clothes()


if __name__ == "__main__":main()