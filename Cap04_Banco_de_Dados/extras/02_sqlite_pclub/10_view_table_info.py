#!/usr/bin/env python3

# -*-coding:utf-8 -*-

"""
   Lendo as informações do banco de dados
   Para ler as informações da tabela usamos o comando PRAGMA.
   Para listar as tabelas do banco usamos o comando SELECT name FROM sqlite_master.
   Para ler o schema da tabela usamos o comando SELECT sql FROM sqlite_master .
   """
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
nome_tabela = 'clientes'

# obtendo informacoes da tabela
cursor.execute('PRAGMA table_info ({})'.format(nome_tabela))

# O método fetchall() retorna o resultado do SELECT.
colunas = [tupla[1] for tupla in cursor.fetchall()]
print('Colunas: ', colunas)

#ou
#for coluna in colunas:
#    print(coluna)

# listando  as tabelas no bd
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print('Tabelas: ')
for tabela in cursor.fetchall():
    print("{}".format(tabela))

# obtendo o schema da tabela
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,))

print('Schema: ')
for schema in cursor.fetchall():
    print('{}'.format(schema))

conn.close()

