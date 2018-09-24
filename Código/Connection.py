import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='127.0.0.1',
                                       database='aula',
                                       user='root',
                                       password='q1w2e3')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()


#import mysql.connector as mysql

#def initDbConfig():
#    dbConfig = {
#                'user':'',
 #               'password':'', #password='admin'
  #              'host':'',
   #             'database':''
    #           }
    # unpack dictionary credencials
    #conn = mysql.connect(**dbConfig)
    #print(conn)
    #conn.close