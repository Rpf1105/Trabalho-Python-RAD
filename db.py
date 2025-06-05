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


def queryExec(query, obj):
    msg = "Operação realizada com sucesso"
    con = connectDb()
    cursor = con.cursor()
    try:
        cursor.execute(query, vars(obj))
        con.commit()
    except TypeError:
        cursor.execute(query, obj)
        con.commit()
    except conector.errors.UniqueViolation:
        msg = "Chave primaria ja existe"
    except conector.errors.ForeignKeyViolation:
        msg = "Violação de chave estrangeira, ou referencia não existe ou foi tentado apagar uma linha que possui dependencias"
        print("fk violation")
    finally:
        cursor.close()
        con.close()
        return msg



def returnSelect(query, obj=None):
    con = connectDb()
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
def verifySimNota(nota):
    if 0 <= nota <= 1:
        return True
def verifyAvNota(nota):
    if 0 <= nota <= 10:
        return True
def checkAprovado():
    return


connectDb()
print(verifySimNota(0))