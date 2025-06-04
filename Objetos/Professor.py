import db
from db import queryExec, connectDb, returnSelect


class Professor:
    def __init__(self, email, codigo=""):
        self.email = email
        self.codigo = codigo
    def insert(self):
        query = '''INSERT INTO public.Docentes VALUES(%(email)s, %(codigo)s);'''
        queryExec(query, self)
    def update(self):
        query = '''UPDATE public.Docentes SET nome = :nome WHERE Código = :%(codigo)s'''
    def delete(self):
        query = '''DELETE FROM public.Docentes WHERE Código = :%(codigo)s'''
    def selectProf(self):
        query = '''SELECT email FROM public.Docentes WHERE disciplina = %(codigo)s'''
    def selectAll(self):
        query = '''SELECT * FROM public.Docentes'''
        return db.returnSelect(query, self)
    def selectAllDisciplinas(self):
        query = '''SELECT disciplina FROM public.Docentes WHERE professor = %(email)s'''
        return returnSelect(query, self)
