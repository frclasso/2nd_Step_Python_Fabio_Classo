#!/usr/bin/python


class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quaaaaaaak!')

    def walk(self):
        print("Walk like a Duck!")

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)


def main():
    donald = Duck(feet=2, color='blue', wings=2)
    print(donald.get_variable('feet'))
    print(donald.get_variable('color'))
    donald.set_variable('color', 'gray')
    print("Changing Donald color to ", donald.get_variable('color'))
    print(donald.get_variable('wings'))



if __name__ == "__main__":main()