
Guia rapido de comandos SQLite3
===============================

---Siga os passos abaixo no TERMINAL-----
-----------------------------------------

Caso nao tenha o sqlite3 instalado, baixar e instalar: https://www.sqlite.org/download.html

1) Para criar um banco de dados,abra o terminal, pode ser no PyCharm, e digite o comando:

**sqlite3 clientes.db**    (pode ser outro nome para o banco de dados).


2) Criando a tabela clientes:

+ sqlite> CREATE TABLE clientes(
    + id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    + Nome VARCHAR(100) NOT NULL,
    + CPF VARCHAR(11) NOT NULL,
    + Email VARCHAR(20) NOT NULL,
    + Fone VARCHAR(20),
    + UF VARCHAR(2) NOT NULL
    + );

3) Para visualizar  o codigo SQL que a tabela criou:
sqlite> **.schema** clientes

4) Para visualizar todas as tabelas existentes:
sqlite>**.tables**

5) Para sair do SQLite3:
sqlite> **.quit**

6) Para economizar tempo, importe os comandos do arquivo "inserirdados.sql" para o banco:
**sqlite3 clientes.db < inserirdados.sql**

7) Abra o sqlite novamente e virifque os dados:
sqlite3 clientes.db
sqlite> **SELECT * FROM cientes;**

8) Voce pode exibir os nomes das colunas e em formato de coluna:
sqlite > **.header on**
sqlite> **.mode column**

9) Para escrever o resultado em um **arquivo externo**:
sqlite>**.output** resultado.txt
sqlite> SELECT * FROM clientes;
sqlite>.exit
cat resultado (unix)

10) Adcionando nova coluna (bloqueado) a tabela clientes:
**sqlite> ALTER TABLE  clientes ADD COLUMN bloqueado Boolean;**

11) Visualizando as informacoes  da tabela clientes:
sqlite>**PRAGMA  table_info**(clientes)

12) Deletando registros:
sqlite> DELETE FROM clientes WHERE id=4;

13) Fazendo **Backup** do Banco:
sqlite3 clientes.db **.dump > clientes.sql**

14) Caso necessite ajuda:
sqlite>**.help**
