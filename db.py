import string
from datetime import datetime
import random
import psycopg2 as conector
from cryptography.fernet import Fernet


def connectDb():
    try:
        con = conector.connect(
            database="TrabalhoRad",
            user='postgres',
            password='senha',
            host='localhost',
            port='5432'
        )
        return con
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)
        connectDb()
def closeDb(con):
    con.close()


def queryExec(con, query, obj):
    cursor = con.cursor()
    try:
        cursor.execute(query, vars(obj))
        con.commit()
    except TypeError:
        cursor.execute(query, obj)
        con.commit()
    except conector.errors.UniqueViolation:
        print("Chave primaria ja existe")
    except conector.errors.ForeignKeyViolation:
        print("Chave estrangeira não encontrada")

    finally:
        cursor.close()
        con.close()

def returnSelect(con, query, obj=None):
    cursor = con.cursor()
    try:
        cursor.execute(query)
    except conector.errors.SyntaxError:
        try:
            con.rollback()
            cursor.execute(query, vars(obj))
        except:
            con.rollback()
            cursor.execute(query, obj)

    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

connectDb()
