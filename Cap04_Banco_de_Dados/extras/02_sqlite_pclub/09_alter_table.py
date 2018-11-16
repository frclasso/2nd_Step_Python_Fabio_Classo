#!/usr/bin/env python3

# -*-coding:utf-8 -*-

import sqlite3

"""
Para inserir uma nova coluna na tabela usamos 
o comando SQL ALTER TABLE.
"""

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# adicionando uma nova coluna a tabela clientes
cursor.execute("""
ALTER TABLE clientes ADD COLUMN bloqueado BOOLEAN;
""")

conn.commit()
print('Novo campo adicionado com sucesso.')
conn.close()