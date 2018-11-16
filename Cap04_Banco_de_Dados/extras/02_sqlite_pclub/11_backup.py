#!/usr/bin/env python3

# -*-coding: utf-8 -*-

import sqlite3
import io

"""Observe o uso da biblioteca io que salva os dados num arquivo
 externo através do método write, e o método iterdump() que exporta 
 a estrutura e dados da tabela para o arquivo externo."""

conn = sqlite3.connect('clientes.db')

with io.open('clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('{}\n'.format(linha))

print('Backup realizado com sucesso.')
print('Salvo como clientes_dump.sql')

conn.close()
