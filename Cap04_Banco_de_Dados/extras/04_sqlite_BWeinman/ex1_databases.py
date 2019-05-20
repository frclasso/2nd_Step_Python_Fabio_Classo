#!/usr/bin/python


import sqlite3


def main():

    db = sqlite3.connect('data1.db')
    db.row_factory = sqlite3.Row
    db.execute('drop table if exists test')
    db.execute('create table test( Nome text, idade int)')
    db.execute('insert into test(Nome, idade) values (?, ?)', ('Fabio', 44))
    db.execute('insert into test(Nome, idade) values (?, ?)', ('Juliana', 41))
    db.execute('insert into test(Nome, idade) values (?, ?)', ('Erick', 10))
    db.execute('insert into test(Nome, idade) values (?, ?)', ('Giovanna', 6))
    db.commit()
    cursor = db.execute('select idade, Nome from test order by idade')
    for row in cursor:
        #print(dict(row))
        print(row['Nome'],'=>', row['idade'])


if __name__ == "__main__":main()