import db


class Funcionario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = False
    def insert(self):
        query = '''INSERT INTO public.funcionários VALUES(%(email)s, %(nome)s, %(senha)s, %(admin)s);'''
    def update(self):
        query = '''UPDATE public.funcionários SET nome = :nome WHERE Código = :%(codigo)s'''
    def delete(self):
        query = '''DELETE FROM public.funcionários WHERE Código = :%(codigo)s'''
    def select(self):
        query = '''SELECT * FROM public.funcionários WHERE Código = %(codigo)s'''
    def selectAll(self):
        query = '''SELECT * FROM public.Disciplina'''
        return db.returnSelect(db.connectDb(), query, self)
