#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import sqlite3


class ClientesDB(object):
    def __init__(self):
        self.db = Connect('clientes.db')

    def close_connection(self):
        self.db.close_db()


class Connect(object):

    def __init__(self, db_name):
        try:
            # conectando
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # imprimindo nome do banco
            print('Database: ',db_name)
            # lendo a versao do sqlite
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            # imprimindo a versao do SQLite
            print('SQLite version: {}'.format(self.data))
        except sqlite3.Error:
            print('Erro ao abrir banco.')
            return False

    def close_db(self):
        if self.conn:
            self.conn.close()
            print('Conexao fechada.')


if __name__=="__main__":
    clientes = ClientesDB()
    clientes.close_connection()