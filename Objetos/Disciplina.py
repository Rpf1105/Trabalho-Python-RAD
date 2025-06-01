from db import connectDb, returnSelect, queryExec


class Disciplina:
    def __init__(self, nome, codigo, ano, semestre):
        self.nome = nome
        self.codigo = codigo
        self.ano = ano
        self.semestre = semestre
    def insert(self):
        query = '''INSERT INTO public.Disciplina(Nome, Código, Ano, Semestre) VALUES(%(nome)s, %(codigo)s, %(ano)s, %(semestre)s);'''
        return queryExec(connectDb(), query, self)
    def update(self):
        query = '''UPDATE public.Disciplina SET nome = :nome WHERE Código = :%(codigo)s'''
        return queryExec(connectDb(), query, self)
    def delete(self):
        query = '''DELETE FROM public.Disciplina WHERE Código = :%(codigo)s'''
        return queryExec(connectDb(), query, self)
    def select(self):
        query = '''SELECT * FROM public.Disciplina"WHERE Código = %(codigo)s'''
        return returnSelect(connectDb(), query, self)
    def selectAll(self):
        query = '''SELECT * FROM public.Disciplina'''
        return returnSelect(connectDb(),query,self)
