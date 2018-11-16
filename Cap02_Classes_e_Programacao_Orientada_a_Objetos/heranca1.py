#!/usr/bin/env python3


class Parent: # define a parent class
    parentAttr = 100 # class attribute

    def __init__(self): # class constructor
        print("Calling parent constructor")

    def parentMethod(self): # class method
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute: ", Parent.parentAttr)


class Child(Parent):  # define a child class
    def __init__(self): # sobrescreve construtor da classe base
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")


c = Child() # define a instance of child
c.childMethod() # child calls its method
c.parentMethod() # calls parent's method
c.setAttr(200) # again calls parent's method
c.getAttr() # again calls parent's method

