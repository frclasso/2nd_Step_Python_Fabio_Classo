#!/usr/bin/env python3

# -*-coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# solicitando os dados do usuario
p_nome = input('Nome: ')   # Caso use Python 2 use o método raw_input()
p_idade = input('Idade: ')
p_cpf = input('CPF: ')
p_email = input('Email: ')
p_fone = input('Telefone: ')
p_cidade = input('Cidade: ')
p_uf = input('UF: ')
p_criado_em = input('Criado em (yyyy-mm-dd): ')

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes(nome, idade, cpf, email, cidade, uf, criado_em)
VALUES(?,?,?,?,?,?,?)
""", (p_nome, p_idade, p_cpf, p_email, p_cidade, p_uf, p_criado_em))

conn.commit()
print('Dados inseridos com sucesso!')
conn.close()