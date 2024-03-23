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

# SELECT
resultado = select("id_aluno, nome, cidade", "alunos")
print(resultado)

# Fiz essa pequena implementação para fins estéticos...
for i in range(len(resultado)):
    print(f"ID - {resultado[i]["id_aluno"]:02} | Nome - {resultado[i]["nome"]}")

# INSERT
#values = [
#    "DEFAULT, 'João Pedro', '2000-02-25', 'Av Bernardo Vieira, 08', 'Macaíba', 'RN', 12345678910",
#    "DEFAULT, 'Marcos Pedro', '2000-02-25', 'Av Bernardo Vieira, 08', 'Macaíba', 'RN', 12345678944"
#]
#insert(values, "alunos")
print(select("*", "alunos", "cidade = 'Macaíba'"))

# UPDATE
# update({"nome":"Túlio Lemos", "cidade":"Macau", "estado":"RN"}, "alunos", "id_aluno = 8")
update({"cpf":"14137719602"}, "alunos", "id_aluno = 8")
print(select("*", "alunos", "cidade = 'Macau'"))

# DELETE (deixei desabilitado por motivos óbvios)
# delete("alunos", "id_aluno = 9")