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
def gerarMatricula():
    date = datetime.today()
    matricula = date.strftime('%Y%m')
    matricula +=  ''.join(random.choice(string.digits) for _ in range(6))
    return matricula

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.matricula = gerarMatricula()
    def insert(self, con):
        query = '''INSERT INTO public.Aluno VALUES(%(nome)s, %(matricula)s)'''
        queryExec(con, query, self)
    def update(self, con):
        query = '''UPDATE Aluno SET nome = :nome WHERE matricula = :matricula'''
    def delete(self, con):
        query = '''DELETE FROM Aluno WHERE matricula = :matricula'''
    def select(self, con):
        query = '''SELECT * FROM Aluno WHERE matricula = :matricula'''

class Disciplina:
    def __init__(self, nome, codigo, ano, semestre):
        self.nome = nome
        self.codigo = codigo
        self.ano = ano
        self.semestre = semestre
    def insert(self, con):
        query = '''INSERT INTO public.Disciplina(Nome, Código, Ano, Semestre) VALUES(%(nome)s, %(codigo)s, %(ano)s, %(semestre)s);'''
        queryExec(con, query, self)
    def update(self, con):
        query = '''UPDATE public.Disciplina SET nome = :nome WHERE Código = :%(codigo)s'''
    def delete(self, con):
        query = '''DELETE FROM public.Disciplina WHERE Código = :%(codigo)s'''
    def select(self, con):
        query = '''SELECT * FROM public.Disciplina"WHERE Código = %(codigo)s'''
        return returnSelect(con, query, self)
    @staticmethod
    def selectAll(con):
        query = '''SELECT * FROM public.Disciplina'''
        return returnSelect(con, query)

class Inscricao:
    def __init__(self, aluno, disciplina):
        self.aluno = aluno
        self.disciplina = disciplina
        self.sim1 = ""
        self.sim2 = ""
        self.av = ""
        self.avs = ""
    def insert(self, con):
        query = '''INSERT INTO public.Inscrição(Aluno,Disciplina) VALUES(%(aluno)s, %(disciplina)s)'''
        queryExec(con, query, self)
    def update(self, con):
        self.avescolha = input("Digite o nome da av a registrar a nota (sim1, sim2, av, avs): ").lower()
        query = '''UPDATE Inscrição SET :avescolha = :nota WHERE disciplina = :disciplina AND aluno = :aluno'''
    def delete(self, con):
        query = '''DELETE FROM Inscrição WHERE disciplina = :disciplina AND aluno = :aluno'''
    def select(self, con):
        query = '''SELECT * FROM public.Inscrição WHERE Disciplina = %(disciplina)s AND Aluno = %(aluno)s'''
        return returnSelect(con, query, self)
    def selectAllAluno(self, con):
        query = '''SELECT * FROM public.Inscrição WHERE Aluno = %(aluno)s'''
        return returnSelect(con, query, self)
    def selectAllDisciplina(self, con):
        query = '''SELECT * FROM public.Inscrição WHERE "Disciplina" = %(disciplina)s'''
        return returnSelect(con, query)

class Funcionario:
    def __init__(self, nome, email, senha, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
    def insert(self, con):
        query = '''INSERT INTO public.funcionários VALUES(%(email)s, %(nome)s, %(senha)s, %(cargo)s)'''
        queryExec(con, query, self)
    def update(self, con):
        query = '''UPDATE public.funcionários SET senha = %(senha)s WHERE email = %(email)s'''
    def delete(self, con):
        query = '''DELETE FROM public.funcionários WHERE email = %(email)s'''
    def select(self, con):
        query = '''SELECT * FROM public.funcionários WHERE email = %(email)s'''

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
