import random
import string
from datetime import datetime

from db import queryExec, connectDb, returnSelect


class Aluno:
    def __init__(self, nome, matricula=None):
        self.nome = nome
        if matricula is None:
            self.matricula = self.gerarMatricula()
        else:
            self.matricula = matricula
    def insert(self):
        query = '''INSERT INTO public.Aluno VALUES(%(nome)s, %(matricula)s)'''
        return queryExec(connectDb(), query, self)
    def update(self):
        query = '''UPDATE Aluno SET nome = :nome WHERE matricula = :matricula'''
        return queryExec(connectDb(), query, self)
    def delete(self):
        query = '''DELETE FROM Aluno WHERE matricula = :matricula'''
        return queryExec(connectDb(), query, self)
    def select(self):
        query = '''SELECT * FROM Aluno WHERE matricula = :matricula'''
        return returnSelect(connectDb(), query, self)
    def gerarMatricula(self):
        date = datetime.today()
        matricula = date.strftime('%Y%m')
        matricula += ''.join(random.choice(string.digits) for _ in range(6))
        return matricula