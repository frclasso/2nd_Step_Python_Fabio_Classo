#!/usr/bin/env python3

from numpy import *

a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])

print(a[:3,[0,1]])

""":3 seleciona de 0 ao 3 elemento do array, 
[0,1] selecionam o primeiro e segundo elementos de cada lista."""