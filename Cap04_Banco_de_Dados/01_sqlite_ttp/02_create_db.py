#!/usr/bin/env python3
"""Following Python program will be used to create a
 table in the previously created database."""

import sqlite3

# cria test.db e concecta
conn = sqlite3.connect('test.db')
print('Opened database successfully.')

# cria tabela company
conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY NOT NULL,
             NAME  TEXT NOT NULL,
             AGE   INT  NOT NULL,
             ADDRESS CHAR(50),
             SALARY REAL);''')


print('Table created successfully.')
conn.close()