#!/usr/bin/env python3

# -*-coding:utf-8 -*-
import sqlite3

# conectado ao banco de dados(database)
conn = sqlite3.connect('clientes.db')

# definindo um cursor
cursor = conn.cursor()

# criando uma tabela (schema)
cursor.execute("""
CREATE TABLE clientes(
     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     nome TEXT NOT NULL,
     idade INTEGER,
     cpf VARCHAR(11) NOT NULL,
     email TEXT NOT NULL,
     fone TEXT,
     cidade TEXT,
     uf VARCHAR(2) NOT NULL,
     criado_em DATE NOT NULL
     );
 """)

print('Tabela clientes criada com sucesso.')
# desconectando
conn.close()

# PARA EXECUTAR NO TERMINAL:
# sqlite3 clientes.db '.tables'
# sqlite3 clientes.db 'PRAGMA table_info(clientes)'