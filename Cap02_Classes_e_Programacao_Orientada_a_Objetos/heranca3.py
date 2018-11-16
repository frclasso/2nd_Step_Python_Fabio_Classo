#!/usr/bin/env python3


class Parent:
    def myMethod(self):
        print("Calling parent method")


class Child(Parent):
    def myMethod(self):
        print("Calling child method")

c = Child()  # Alterne para Parent() e veja o resultado
c.myMethod()