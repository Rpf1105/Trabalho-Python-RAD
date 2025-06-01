import db
from db import queryExec, connectDb


class Professor:
    def __init__(self, email, codigo):
        self.email = email
        self.codigo = codigo
    def insert(self):
        query = '''INSERT INTO public.Docentes VALUES(%(email)s, %(codigo)s);'''
        queryExec(connectDb(), query, self)
    def update(self):
        query = '''UPDATE public.Disciplina SET nome = :nome WHERE Código = :%(codigo)s'''
    def delete(self):
        query = '''DELETE FROM public.Disciplina WHERE Código = :%(codigo)s'''
    def select(self):
        query = '''SELECT * FROM public.Disciplina"WHERE Código = %(codigo)s'''
    def selectAll(self):
        query = '''SELECT * FROM public.Disciplina'''
        return db.returnSelect(db.connectDb(), query, self)
