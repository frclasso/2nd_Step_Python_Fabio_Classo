#!/usr/bin/env python3

from numpy import *

Alunos = array([['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave',80,80,80,90,95]])

Alunos = append(Alunos,[['Sam',82,79,88,97,99]],axis=0)

"""aqui axis representa as dimensões onde 0
significa linha(row) e 1 significa coluna(column)."""

print(Alunos)