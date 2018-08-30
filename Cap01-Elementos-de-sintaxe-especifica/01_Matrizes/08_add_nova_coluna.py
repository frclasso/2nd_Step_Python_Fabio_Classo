#!/usr/bin/env python3

from numpy import *

Aluno = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]])

Aluno = insert(Aluno,[6],[[73],[80],[85]], axis=1)

"""aqui axis representa as dimensões onde 0
significa linha(row) e 1 significa coluna(column)."""

print(Aluno)