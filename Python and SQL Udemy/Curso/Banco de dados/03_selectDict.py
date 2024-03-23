# Resolvi destacar essa maneira pois retorna os valores em dicionários que são mais fáceis de trabalhar.

import MySQLdb

def select(fields, tables, where=None):
    global c
    query = "SELECT " + fields + " FROM " + tables

    if (where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()

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

resultado = select("id_aluno, nome, cidade", "alunos")
print(resultado)

# Fiz essa pequena implementação para fins estéticos...
for i in range(len(resultado)):
    print(f"ID - {resultado[i]["id_aluno"]:02} | Nome - {resultado[i]["nome"]}")
