#!/usr/bin/env python3

# -*-coding:utf-8-*-


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        """Recebe os valores para os lados"""
        self.sides = [float(input('Enter side: '+str(i+1)+" : "))for i in range(self.n)]

    def dispSides(self):
        """Exibe os valores dos lados"""
        for i in range(self.n):
            print('Side', i+1, 'is', self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
       # super().__init__(3)

    def findArea(self):
        """Calcula a area do triangulo"""
        a,b,c  = self.sides
        # calculate the semi-perimeter
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c)) **0.5
        print('The area of the Triangle is %0.2f'% area)

t = Triangle()
# t.inputSides()
# t.dispSides()
#
# t.findArea()

print(isinstance(t, Triangle))