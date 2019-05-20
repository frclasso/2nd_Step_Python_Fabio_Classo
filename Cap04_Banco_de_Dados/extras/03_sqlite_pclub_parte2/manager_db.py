#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import os
import sqlite3
import io
import datetime
import names
import csv
import random
from gen_random_values import *


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

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print('Conexao fechada.')


class ClientesDB(object):

    tb_name = 'clientes' # nome da tabela a ser criada

    def __init__(self):
        self.db = Connect('clientes.db')
        self.tb_name

    def criar_schema(self, schema_name='clientes_schema.sql'): # tem q ter esse arquivo
        print("Criando tabela {}".format(self.tb_name))

        try:
            with open(schema_name, 'rt') as f:
                schema =f.read()
                self.db.cursor.executescript(schema) #  com cursor.executescript() executamos a instrução sql que está dentro do arquivo.
        except sqlite3.Error:
            print("Aviso:  A tabela {} ja existe.".format(self.tb_name))
            return False
        print("Tabela criada com sucesso.")

    def inserir_um_registro(self):
        """A função a seguir insere um registro na tabela. Repare no uso do comando self.db.commit_db()
         que grava de fato os dados."""
        try:
            self.db.cursor.execute("""
            INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES('Regis da Silva', 35, '1234567809', 'regis@email.com','(11)9999-8888',
            'Sao Paulo', 'SP', '2016-07-30 11:23:00.199000')
            """)
            # gravando no bd
            self.db.commit_db()
            print("Um registro inserido com sucesso.")
        except sqlite3.IntegrityError:
            print('Aviso: o email deve ser unico (1).')
            return False

    def inserir_com_lista(self):
        """A função a seguir insere vários registros a partir de uma lista.
        Repare no uso do comando executemany(sql, [parâmetros]que executa a instrução sql
        várias vezes. Note também, pela sintaxe, que a quantidade de ? deve ser igual a
        quantidade de campos, e o parâmetro, no caso está sendo a lista criada.)
        """
        # criando uma lista de dados
        lista = [('Agenor de Sousa', 23, '12345678901', 'agenor@email.com',
              '(10) 8300-0000', 'Salvador', 'BA', '2014-07-29 11:23:01.199001'),
             ('Bianca Antunes', 21, '12345678902', 'bianca@email.com',
              '(10) 8350-0001', 'Fortaleza', 'CE', '2014-07-28 11:23:02.199002'),
             ('Carla Ribeiro', 30, '12345678903', 'carla@email.com',
              '(10) 8377-0002', 'Campinas', 'SP', '2014-07-28 11:23:03.199003'),
             ('Fabiana de Almeida', 25, '12345678904', 'fabiana@email.com',
              '(10) 8388-0003', 'São Paulo', 'SP', '2014-07-29 11:23:04.199004'),
             ]
        try:
            self.db.cursor.executemany("""
            INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf,criado_em)
            VALUES(?,?,?,?,?,?,?,?)
            """, lista)
            # gravando no banco de dados
            self.db.commit_db()
            print("Dados da lista inseridos com sucesso: {} registros".format(len(lista)))
        except sqlite3.IntegrityError:
            print('Aviso: o email deve ser unico (2).')
            return False

    def inserir_de_arquivo(self):
        """Também podemos escrever as instruções sql num arquivo externo
        (clientes_dados.sql) e executá-lo com o comando executescript(sql_script). """
        try:
            with open('clientes_dados.sql', 'rt') as f: # tem q ter esse arquivo
                dados = f.read()
                self.db.cursor.executescript(dados)
                # gravando no banco de dados
                self.db.commit_db()
                print('Dados do arquivo {} inseridos com sucesso.'.format(f[1]))
        except sqlite3.IntegrityError:
            print('Aviso: o email deve ser unico (3).')
            return False

    def inserir_de_csv(self, file_name='clientes.csv'):
        """Agora vamos importar os dados de clientes.csv
         tem q ter esse arquivo ou gerar com gen_csv.py
         A única novidade é o comando csv.reader()
        """
        try:
            reader = csv.reader(open(file_name,'rt'), delimiter=',')
            linha=(reader,)
            for linha in reader:
                self.db.cursor.execute("""
                INSERT INTO clientes(nome, idade, cpf, email,fone, cidade, uf, criado_em)
                VALUES(?,?,?,?,?,?,?,?)
                """, linha)
            # gravando no banco de dados
            self.db.commit_db()
            print('Dados importados com sucesso.')
        except sqlite3.IntegrityError:
            print("Aviso: o email deve ser unico (4).")
            return False

    def inserir_com_parametros(self):
        """ Quando falamos parâmetros de entrada significa interação direta do
        usuário na aplicação. Ou seja, vamos inserir os dados diretamente pelo
        terminal em tempo de execução. Para isso nós usamos o comando input()
        para Python 3 ou raw_input() para Python 2."""

        # solicitando os dados do usuario
        self.nome = input("Nome: ")
        self.idade = input("Idade: ")
        self.cpf = input("CPF: ")
        self.email = input("Email: ")
        self.fone = input("Telefone: ")
        self.cidade = input("Cidade: ")
        self.uf = input("UF: ") or 'SP'
        date = datetime.datetime.now().isoformat(" ")
        self.criado_em = input("Criado em : {}".format(date) or date)

        try:
            self.db.cursor.execute("""
            INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES(?,?,?,?,?,?,?,?)
            """, (self.nome, self.idade, self.cpf,self.email,self.fone,
                  self.cidade,self.uf,self.criado_em))
            # gravando no banco de dados
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: o email deve ser unico (5).")
            return False

    def inserir_dados_randomicos(self, repeat=10):
        """Inserir registros com valores randomicos names """
        lista = []
        for i in range(repeat):
            date  = datetime.datetime.now().isoformat( " ")
            fname = names.get_first_name()
            lname = names.get_last_name()
            name = fname + ' ' + lname
            email = fname[0].lower() + '.' + lname.lower() + '@email.com'
            c = gen_city()
            city = c[0]
            uf = c[1]
            # nome, idade, cpf, email, fone, cidade, uf, criado_em
            lista.append((name, gen_age(), gen_cpf(),
                              email, gen_phone(),
                              city, uf, date))
        try:
            self.db.cursor.executemany("""
            INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES(?,?,?,?,?,?,?,?)
            """,lista)
            self.db.commit_db()
            print("Inserindo {} registros na tabela ...  ".format(repeat))
            print("Registros criados com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: o email deve ser unico (6).")
            return False

    def ler_todos_clientes(self):
        sql = 'SELECT * FROM clientes ORDER BY nome'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def imprimir_todos_clientes(self):
        """Imprime dados da tabela formatados"""
        lista = self.ler_todos_clientes()
        print('{:>3s} {:20s} {:<5s} {:15s} {:21s} {:14s} {:15s} {:s}'.format(
            'id', 'nome', 'idade', 'cpf', 'email', 'cidade', 'uf', 'criado_em'
        ))
        for c in lista:
            print('{:3d} {:23s} {:2} {:s} {:>25s} {:s} {:15s} {:s} {:s}'.format(
                c[0], c[1], c[2],
                c[3], c[4], c[5],
                c[6], c[7], c[8]
            ))

    def imprimir_sem_formatar(self):
        """Imprime dados da tabela sem uso formatacao"""
        lista = self.ler_todos_clientes()
        for c in lista:
            print(c)

    def localizar_cliente(self, id):
        """a seguir como localizar um cliente pelo id. Uma sutileza é a vírgula
        logo depois do id, isto é necessário porque quando usamos a ? é esperado
         que os parâmetros sejam uma tupla."""
        r = self.db.cursor.execute(
            'SELECT * FROM clientes WHERE id= ?', (id,))
        return r.fetchone()

    def imprimir_cliente(self, id):
        if self.localizar_cliente(id) == None:
            print("Nao existe cliente com id informado, {}".format(id))
        else:
            print(self.localizar_cliente(id))

    def contar_clientes(self):
        r = self.db.cursor.execute(
            'SELECT COUNT(*) FROM clientes')
        print("Total de clientes: ", r.fetchone()[0])

    def contar_clientes_por_idade(self, t=50):
        r = self.db.cursor.execute('SELECT COUNT(*) FROM clientes WHERE idade > ?', (t,))
        print("Quantidade de clientes maiores que",t, "anos:",r.fetchone()[0])

    def localizar_cliente_por_idade(self, t=50):
        resultado = self.db.cursor.execute(
            'SELECT * FROM clientes WHERE idade > ?',(t,))
        print("Clientes maiores que", t, "anos:")
        for cliente in resultado.fetchall():
            print(cliente)

    def localizar_cliente_por_uf(self, t='SP'):
        resultado = self.db.cursor.execute(
            'SELECT * FROM clientes WHERE uf = ?', (t,))
        print('Clientes  de estado de', t, ":")
        for cliente in resultado.fetchall():
            print(cliente)

    def meu_select(self, sql="SELECT * FROM clientes WHERE uf='RJ';"):
        r = self.db.cursor.execute(sql)
        # caso queira gravar os dados, se usar INSERT, UPDATE ou DELETE
        self.db.commit_db()
        for cliente in r.fetchall():
            print(cliente)

    def atualizar(self, id):
        try:
            c = self.localizar_cliente(id) # re-uso de funcao
            if c:
                # solicitando os dados do usuario
                self.novo_fone = input('Fone: ')
                self.db.cursor.execute("""
                UPDATE clientes
                SET fone = ?
                WHERE id=?
                """, (self.novo_fone, id, ))
                # gravando dados no banco de dados
                self.db.commit_db()
                print('Dados atualizados com sucesso.')
            else:
                print("Nao existe cliente com o id informado {}.".format(id))
        except Exception as e:
            raise e

    def deletar(self, id):
        """Deleta um registro da tabela, localiza por ID"""
        try:
            c = self.localizar_cliente(id)
            if c:
                self.db.cursor.execute("""
                DELETE FROM clientes WHERE id=?
                """, (id,))
                # gravando no banco de dados
                self.db.commit_db()
                print("Registro {} excluido com sucesso.".format(id))
            else:
                print('Nao existe cliente com o codigo informado: {}'.format(id))

        except Exception as e:
            raise e

    def alterar_tabela(self):
        """Uso da funcao ALTER TABLE, para adicionar uma nova coluna."""
        try:
            self.db.cursor.execute("""
            ALTER TABLE clientes 
            ADD COLUMN bloqueado BOOLEAN;
            """)
            # gravando no banco de dados
            print("Novo campo adicionado com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: o campo bloqueado ja existe.")
            return False

    def table_info(self):
        """Para exibir informacoes da tabela"""
        t = self.db.cursor.execute(
            'PRAGMA table_info({})'.format(self.tb_name))
        colunas = [tupla[1] for tupla in t.fetchall()]
        print('Colunas: ', colunas)

    def table_list(self):
        """Listando as tabelas do BD."""
        l = self.db.cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
        """)
        print('Tabelas: ')
        for tabela in l.fetchall():
            print('{}'.format(tabela))

    def table_schema(self):
        """Obtendo o schema da tabela"""
        s = self.db.cursor.execute("""
        SELECT sql FROM sqlite_master WHERE type='table' AND name=?
        """, (self.tb_name,))
        print('Schema: ')
        for schema in s.fetchall():
            print('{}'.format(schema))

    def backup(self, file_name='clientes_bkp.sql'):
        """Realiza bcackup, outro nome pode ser passado como paramentro"""
        with io.open(file_name, 'w') as f:
            for linha in self.db.conn.iterdump():
                f.write('%s\n'% linha)
        print('Backup realizado com sucesso.')
        print('Salvo como {}'.format(file_name))

    def recuperar_dados(self, db_name='clientes_recovery.db', file_name='clientes_bkp.sql'):
        """Recupera dados atraves do arquiv clientes_bkp.sql"""
        try:
            self.db = Connect(db_name)
            f = io.open(file_name, 'r')
            sql = f.read()
            self.db.cursor.executescript(sql)
            print('Banco de dados recuperado com sucesso.')
            print('Salvo com {}'.format(db_name))
        except sqlite3.OperationalError:
            print("Aviso: o banco de dados {} ja existe."
                  "Exclua-o e faca novamente.".format(db_name))
            return False

    def close_connection(self):
        """Fechando conexao"""
        self.db.close_db()

# Vamos criar uma outra instância chamada PessoasDb().
# Neste exemplo vamos relacionar duas tabelas: pessoas e cidades.


class PessoasDb(object):

    tb_name = 'pessoas'

    def __init__(self):
        self.db = Connect('pessoas.db')
        self.tb_name

    def criar_schema(self, schema_name='pessoas_schema.sql'): # tem q ter esse arquivo
        print('Criando tabela {}'.format(self.tb_name))

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print("Aviso: a tabela {} ja existe.".format(self.tb_name))
            return False
        print("Tabela {} criada com sucesso.".format(self.tb_name))

    def inserir_de_csv(self, file_name='cidades.csv'):
        """Inserindo a partir de cidades.csv"""
        try:
            c =csv.reader(
                open(file_name, 'rt'), delimiter=',')
            t = (c,)
            for t in c:
                self.db.cursor.execute("""
                INSERT INTO cidades(cidade, uf)VALUES (?,?)
                """, t)
            # gravando no banco de dados
            self.db.commit_db()
            print("Dados importados do csv com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: a cidade deve ser unica.")
            return False

    def gen_cidade(self):
        """Conta quantas cidades estao cadastradas e escolhe uma pelo ID"""
        sql = 'SELECT COUNT (*) FROM cidades'
        q = self.db.cursor.execute(sql)
        return q.fetchone()[0]

    def inserir_randomico(self, repeat=10):
        lista=[]
        for _ in range(repeat):
            fname = names.get_first_name()
            lname = names.get_last_name()
            email =fname[0].lower() + '.' + lname.lower() + '@email.com'
            cidade_id = random.randint(1, self.gen_cidade())
            lista.append((fname, lname, email, cidade_id))
        try:
            self.db.cursor.executemany("""
            INSERT INTO pessoas(nome, sobrenome, email, cidade_id)
            VALUES(?,?,?,?)
            """, lista)
            # salvando
            self.db.commit_db()
            print("Inserindo {} registros na tabela".format(repeat))
            print("Registro s criados com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: o email deve ser unico.")
            return False

    def table_info(self):
        """Para exibir informacoes da tabela"""
        t = self.db.cursor.execute(
            'PRAGMA table_info({})'.format(self.tb_name))
        colunas = [tupla[1] for tupla in t.fetchall()]
        print('Colunas: ', colunas)

    def table_list(self):
        """Listando as tabelas do BD."""
        l = self.db.cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
        """)
        print('Tabelas: ')
        for tabela in l.fetchall():
            print('{}'.format(tabela))

    def table_schema(self):
        """Obtendo o schema da tabela"""
        s = self.db.cursor.execute("""
        SELECT sql FROM sqlite_master WHERE type='table' AND name=?
        """, (self.tb_name,))
        print('Schema: ')
        for schema in s.fetchall():
            print('{}'.format(schema))

    def inserir_uma_pessoa(self):
        try:
            self.db.cursor.execute("""
                   INSERT INTO pessoas(nome, sobrenome, email,cidade_id,criado_em)
                   VALUES('Juliana', 'Classo', 'juju@email.com', '4',
                   '2016-07-30 11:23:00.199000')
                   """)
            # gravando no bd
            self.db.commit_db()
            print("Um registro inserido com sucesso.")
        except sqlite3.IntegrityError:
            print('Aviso: o email deve ser unico (inserir pessoas).')
            return False

    def ler_todas_pessoas(self):
        sql = 'SELECT * FROM pessoas INNER JOIN cidades ON ' \
              'pessoas.cidade_id = cidades.id'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def imprimir_todas_pessoas(self):
        lista = self.ler_todas_pessoas()
        for c in lista:
            print(c)

    def update_pessoa(self, id):
        pass

    def deletar_pessoa(self, id):
        pass

    # myselect imprime todos os nomes que comecam com R
    def myselect(self, sql="SELECT * FROM pessoas WHERE nome LIKE 'E%' ORDER BY nome "):
        r = self.db.cursor.execute(sql)
        # salvando
        self.db.commit_db()
        print("Nomes que comecam com E:")
        for c in r.fetchall():
            print(c)

    def table_list(self):
        # listando as tabelas do BD
        l = self.db.cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
        """)
        print('Tabelas: ')
        for tabela in l.fetchall():
            print('{}'.format(tabela))

    def fechar_conexao(self):
        self.db.close_db()


if __name__=="__main__":
    print()
    print('clientes.db')
    c = ClientesDB()
    #c.criar_schema()
    c.inserir_um_registro()
    # c.inserir_com_lista()
    # c.inserir_de_arquivo()
    # c.inserir_de_csv()
    # c.inserir_com_parametros()
    #c.inserir_dados_randomicos() # Erro no modulo 'names'
    #c.imprimir_todos_clientes()
    #c.imprimir_sem_formatar()
    #c.imprimir_cliente(7)
    #c.contar_clientes()
    #c.contar_clientes_por_idade()
    #c.contar_clientes_por_idade(18) # alterei o valor do parametro 't'
    #c.localizar_cliente_por_idade(97) # alterei o valor do parametro 't'
    #c.localizar_cliente_por_uf('SC')
    #c.meu_select()
    #c.meu_select("SELECT * FROM clientes WHERE uf='RN' ORDER BY nome;")
    #c.atualizar(7)
    #c.deletar(10)
    #c.alterar_tabela()
    #c.table_info()
    #c.table_list()
    #c.table_schema()
    #c.backup()
    #c.recuperar_dados()

    print()
    print('pessoas.db')
    p = PessoasDb()
    #p.criar_schema()
    #p.inserir_de_csv()
    #p.gen_cidade()
    #p.table_info()
    #p.table_list()
    #p.table_schema()
    p.inserir_randomico(100)
    #p.inserir_uma_pessoa() # ok
    p.imprimir_todas_pessoas()
    #p.myselect() #ok
    #p.table_list() #ok
    #p.fechar_conexao()