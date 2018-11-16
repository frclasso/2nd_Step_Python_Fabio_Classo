#!/usr/bin/env python3

# -*-coding:utf-8 -*-
"""Aqui nós usamos  SELECT.
O método fetchall() retorna o resultado do SELECT"""

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# lendo dados
cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()