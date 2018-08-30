#!/usr/bin/env python3

from numpy import *

Alunos = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]])

Alunos = delete(Alunos,[1],0)

print(Alunos)