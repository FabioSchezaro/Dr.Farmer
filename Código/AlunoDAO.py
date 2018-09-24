import Connection as c

resp = c.conn.cursor()

def getById(id):
    sql = 'SELECT * FROM aluno WHERE id = ' + str(id)
    resp.execute(sql)
    return resp.fetchone()

def getAll():
    sql = 'SELECT * FROM aluno;'
    resp.execute(sql)
    return resp.fetchall()

def save(nome):
    sql = "INSERT INTO aluno (id, nome) values (auto_increment, '" + nome + "')"
    resp.execute(sql)

def delete(id):
    sql = 'DELETE FROM aluno WHERE id = ' + str(id)
    resp.execute(sql)