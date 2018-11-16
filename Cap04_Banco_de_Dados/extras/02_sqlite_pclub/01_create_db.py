#!/usr/bin/env python3

# -*-coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('clientes.db')
print('Banco de dados clintes.db criado com sucesso.')
conn.close()