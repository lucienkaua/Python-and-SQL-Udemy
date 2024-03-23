import MySQLdb

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

def select(fields, tables, where=None):
    global c
    query = "SELECT " + fields + " FROM " + tables

    if (where):
        query = query + " WHERE " + where
    
    c.execute(query)
    return c.fetchall()

# print(select("nome, cpf", "alunos", "id_aluno = 1"))
print(select("nome, cpf", "alunos"))
