import string
from datetime import datetime
import random
import psycopg2 as conector

def connectDb():
    try:
        conexao = conector.connect(
            database="SistemaNotas",
            user='postgres',
            password='senha',
            host='127.0.0.1',
            port='5432'
        )
        return conexao
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)
        connectDb()

def gerarMatricula():
    date = datetime.today()
    matricula = date.strftime('%Y%m')
    matricula +=  ''.join(random.choice(string.digits) for _ in range(6))
    return matricula
class Aluno:
    def __init__(self, nome, matricula=None):
        self.nome = nome
        if matricula is None:
            self.matricula = gerarMatricula()
        else:
            self.matricula = matricula
    def insert(self, con):
        query = '''INSERT INTO Aluno VALUES(:nome, :matricula)'''
    def update(self, con):
        query = '''UPDATE Aluno SET nome = :nome WHERE matricula = :matricula'''
    def delete(self, con):
        query = '''DELETE FROM Aluno WHERE matricula = :matricula'''
    def select(self, con):
        query = '''SELECT * FROM Aluno WHERE matricula = :matricula'''
