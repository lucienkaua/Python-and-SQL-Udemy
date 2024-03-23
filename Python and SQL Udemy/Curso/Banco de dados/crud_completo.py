import MySQLdb

def select(fields, tables, where=None):
    global c
    query = "SELECT " + fields + " FROM " + tables

    if (where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()


def insert(values, table, fields=None):
    global c, conexao
    query = "INSERT INTO " + table

    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join([" (" + v + ") " for v in values])

    c.execute(query)
    conexao.commit()


def update(sets, table, where=None):
    global c, conexao

    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if (where):
        query = query + " WHERE " + where

    c.execute(query)
    conexao.commit()


def delete(table, where):
    global c, connect

    query = "DELETE FROM " + table + " WHERE " + where
    c.execute(query)
    conexao.commit()

# <------------------------ Main ---------------------------->
host = "localhost"
user = "user"
password = "123456"
db = "escola_cursos"
port = 3306

try:
    conexao = MySQLdb.connect(host, user, password, db, port)
    c = conexao.cursor(MySQLdb.cursors.DictCursor)
    print("Conexão bem sucedida!")
except:
    print("Ocorreu um erro ao tentar conectar. Verifique se os dados estão corretos e tente novamente.")
    quit()
