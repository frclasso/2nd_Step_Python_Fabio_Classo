#!/usr/bin/python

import sqlite3


def insert(db, row):
    db.execute('insert into test (nome, sobrenome, email,cargo) '
               'values (?,?,?,?)', (row['nome'], row['sobrenome'], row['email'], row['cargo']))
    db.commit()


def retrieve(db, nome):
    cursor = db.execute('select * from test where nome = ?', (nome,))
    return cursor.fetchone()


def update(db, row):
    db.execute('update test set email = ? ,cargo = ? where nome = ?', (row['email'],row['cargo'], row['nome']))
    db.commit()


def delete(db, nome):
    db.execute('delete from test where nome = ?', (nome,))
    db.commit()


def disp_rows(db):
    cursor = db.execute('select * from test order by nome')
    for row in cursor:
        print(' {},{} - {} - {}'.format(row['nome'], row['sobrenome'], row['email'], row['cargo']))


def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    print('Create table test___')
    db.execute('drop table if exists test')
    db.execute('create table test (nome text,sobrenome text, email text, cargo text)')

    print()
    print("Create rows_______________________________________")
    insert(db, dict(nome='Fabio', sobrenome='Classo', email='fabioclasso@email.com', cargo='Developer'))
    insert(db, dict(nome='Juliana', sobrenome='Classo', email='juclasso@email.com', cargo='Enfermeira'))
    insert(db, dict(nome='Erick', sobrenome='Classo', email='erickclasso@email.com', cargo='Estudante'))
    insert(db, dict(nome='Giovanna', sobrenome='Classo', email='giclasso@email.com', cargo='Estudante'))
    insert(db, dict(nome='Taissa', sobrenome='Classo', email='taissaclasso@email.com', cargo='Estudante'))
    insert(db, dict(nome='Diva', sobrenome='Reis', email='divareis@email.com', cargo='Costureira'))
    insert(db, dict(nome='Ramiro', sobrenome='Classo', email='ramiroclasso@email.com', cargo='Aposentado'))
    insert(db, dict(nome='John', sobrenome='Doe', email='none@email.com', cargo='desaparecido'))
    insert(db, dict(nome='Jane', sobrenome='Doe', email='none@email.com', cargo='desaparecida'))

    disp_rows(db)

    print()
    print('Retrieve rows_________________________________________')
    print(dict(retrieve(db, 'Fabio')),'\n',dict(retrieve(db, 'Juliana')))
    #
    print()
    print('Update rows_________________________________________')
    update(db, dict(nome='John', sobrenome='Doe', email='johndoe@email.com', cargo='ajudante geral'))
    update(db, dict(nome='Jane', sobrenome='Doe', email='janedoe@email.com', cargo='ajudante geral'))

    disp_rows(db)

    print()
    print('Delete rows_________________________________________')
    delete(db, 'John')
    delete(db, 'Jane')
    disp_rows(db)


if __name__ == "__main__":main()