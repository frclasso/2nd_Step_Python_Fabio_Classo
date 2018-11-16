#!/usr/bin/env python3

# -*-coding:utf-8 -*-

import sqlite3
import io

"""Recuperando o banco de dados (importando dados)
Criaremos um novo banco de dados e iremos reconstruir a tabela e
 os dados com o arquivo clientes_dump.sql. O método read() lê o 
 conteúdo do arquivo clientes_dump.sql e o método executescript() 
 executa as instruções SQL escritas neste arquivo."""

conn = sqlite3.connect('clientes_recuperado.db')
cursor = conn.cursor()

f = io.open('clientes_dump.sql', 'r')
sql = f.read()
cursor.executescript(sql)

print('Banco de dados recuperado com sucesso.')
print('Salvo com clientes_recuperado.db')

conn.close()

# Voce pode usar o programa 06_read_data.py,
#  eh necessario alterar a linha 09, para clientes_recuperado.db