#!/usr/bin/env python3

from numpy import *

Alunos = array([['Roy',80,75,85,90,95,105],
      ['John',75,80,75,85,100,105],
      ['Dave',80,80,80,90,95,105]])

Alunos = delete(Alunos, s_[1::2], axis=1)
# [1::] do segundo elemento(1) pulando um elemento [::2]

print(Alunos)