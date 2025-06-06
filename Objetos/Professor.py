import db
from db import queryExec, connectDb, returnSelect


class Professor:
    def __init__(self, email, codigo=""):
        self.email = email
        self.codigo = codigo
    def insert(self):
        query = '''INSERT INTO public.Docentes VALUES(%(email)s, %(codigo)s);'''
        return queryExec(query, self)
    def update(self):
        query = '''UPDATE public.Docentes SET email = %(email)s WHERE disciplina = %(codigo)s'''
        return queryExec(query, self)
    def delete(self):
        query = '''DELETE FROM public.Docentes WHERE disciplina = %(codigo)s'''
        return queryExec(query, self)
    def selectProf(self):
        query = '''SELECT email FROM public.Docentes WHERE disciplina = %(codigo)s'''
        return  returnSelect(query, self)
    def selectAll(self):
        query = '''SELECT * FROM public.Docentes'''
        return db.returnSelect(query, self)
    def selectAllDisciplinas(self):
        query = '''SELECT disciplina FROM public.Docentes WHERE professor = %(email)s'''
        return returnSelect(query, self)
