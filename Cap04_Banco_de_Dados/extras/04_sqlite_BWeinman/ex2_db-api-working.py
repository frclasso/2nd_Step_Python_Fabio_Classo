#!/usr/bin/env python3

import sqlite3


def main():
    print('connect')
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    cur.execute('DROP TABLE IF EXISTS test')
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY , nome TEXT , sobrenome TEXT, idade INTEGER, email TEXT
            )
            """)
    print('Tabela criada com sucesso, inserindo dados...')
    cur.execute("""
        INSERT INTO test(nome,sobrenome, idade,email) VALUES ('Fabio','Classo', 44, 'fabioclasso@eail.com')
        """)
    cur.execute("""
        INSERT INTO test(nome,sobrenome, idade,email) VALUES ('Juliana','Classo', 41, 'juclasso@email.com')
        """)
    cur.execute("""
        INSERT INTO test(nome,sobrenome, idade,email) VALUES ('Erick', 'Claso',10, 'erick@email.com')
        """)
    print('Salvando os dados (commit)')
    db.commit()
    print('Contando (count)')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'Existem  {count} linhas na tabela.')
    print('Lendo-as...')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print()
    print('Apagando a tabela test (dropping test table)')
    cur.execute('DROP TABLE test')
    print()
    print('Fechando (close)')
    db.close()


if __name__=="__main__":main()