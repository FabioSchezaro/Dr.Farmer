import Connection as c
from mysql.connector import MySQLConnection, Error
from DbConfig import read_db_config

def save(nome, dosagem, tipoDosagem, tipo):

    qry = "INSERT INTO medicamentos (nomeMedicamento, dosagemMedicamento, tipoDosagem, tipoDosagemMedicamento )" \
          "VALUES (%s, %s, %s, %s)"
    vals = (nome, dosagem, tipoDosagem, tipo)

    try:
        config = read_db_config()
        conn = MySQLConnection(**config)

        cursor = conn.cursor()
        cursor.execute(qry, vals)

        conn.commit()
        
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def getById(id):
    sql = 'SELECT * FROM medicamentos WHERE id = ' + str(id)
    cursor.execute(sql)
    return cursor.fetchone()

def getAll():
    sql = 'SELECT * FROM medicamentos'
    cursor.execute(sql)
    return cursor.fetchall()

def delete(id):
    sql = 'DELETE FROM medicamentos WHERE id = ' + str(id)
    cursor.execute(sql)


