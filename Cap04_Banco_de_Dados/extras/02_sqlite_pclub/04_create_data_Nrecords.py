#!/usr/bin/env python3

# -*-coding:uf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

"""Usando uma lista podemos inserir vários registros 
de uma vez, e o método executemany faz essa ação."""

# criando uma lista de dados
lista = [(
    'Fabio', 23, '44444444444', 'fabio@email.com', '1223-3456', 'Florianopolis', 'SC',
    '2014-06-09'),
    ('Joao', 21, '55555555555', 'joao@email.com',
     '11-1234-5600', 'Sao Paulo', 'SP', '2014-06-09'),
    ('Xavier', 24, '66666666666', 'xavier@email.com', '12-1234-5601',
     'Campinas', 'SP', '2014-06-10')
]

# inserindo dados na tabela
cursor.executemany("""
    INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES(?,?,?,?,?,?,?,?)
""", lista)

# Observe o uso de ? isto significa que no lugar de cada ? entrará os valores
# da lista na sua posição respectiva. É o que nós chamamos de parâmetros de entrada.


conn.commit()
print('Dados inseridos com sucesso!')

conn.close()