from db import returnSelect, queryExec
class Disciplina:
    def __init__(self, nome, codigo, ano:int, semestre:int):
        self.nome = nome
        self.codigo = codigo
        self.ano = ano
        self.semestre = semestre
    def insert(self):
        query = '''INSERT INTO public.Disciplina(Nome, Código, Ano, Semestre) VALUES(%(nome)s, %(codigo)s, %(ano)s, %(semestre)s);'''
        return queryExec(query, self)
    def update(self):
        query = '''UPDATE public.Disciplina SET nome = :nome WHERE Código = %(codigo)s'''
        return queryExec(query, self)
    def delete(self):
        query = '''DELETE FROM public.Disciplina WHERE Código = %(codigo)s'''
        return queryExec(query, self)
    def select(self):
        query = '''SELECT * FROM public.Disciplina WHERE Código = %(codigo)s'''
        return returnSelect(query, self)
    def selectNome(self):
        query = '''SELECT nome FROM public.Disciplina WHERE Código = %(codigo)s'''
        return returnSelect(query, self)
    @staticmethod
    def selectAll():
        query = '''SELECT * FROM public.Disciplina'''
        return returnSelect(query)
    def selectAllCod(self):
        query = '''SELECT código FROM public.Disciplina'''
        return returnSelect(query, self)
