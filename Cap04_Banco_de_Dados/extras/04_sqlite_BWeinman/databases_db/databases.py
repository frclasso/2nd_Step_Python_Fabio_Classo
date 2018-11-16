#!/usr/bin/python


import sqlite3


def main():

    db = sqlite3.connect('test.bb')
    db.row_factory = sqlite3.Row
    db.execute('drop table if exists test')
    db.execute('create table test( t1 text, i1 int)')
    db.execute('insert into test(t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test(t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test(t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test(t1, i1) values (?, ?)', ('four', 4))
    db.commit()
    cursor = db.execute('select i1, t1 from test order by i1')
    for row in cursor:
        #print(dict(row))
        print(row['t1'],'=>', row['i1'])


if __name__ == "__main__":main()