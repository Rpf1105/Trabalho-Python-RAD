from db import queryExec, connectDb, returnSelect


class Funcionario:
    def __init__(self, email, senha, nome = "", admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin
    def insert(self):
        query = '''INSERT INTO public.funcionários VALUES(%(email)s, %(nome)s, %(senha)s, %(admin)s);'''
        return queryExec(query, self)
    def update(self):
        query = '''UPDATE public.funcionários SET nome = %(nome)s WHERE email = %(email)s'''
    def delete(self):
        query = '''DELETE FROM public.funcionários WHERE email = %(email)s'''
        return queryExec(query, self)
    def select(self):
        query = '''SELECT nome, email, admin FROM public.funcionários WHERE email = %(email)s'''
    def selectAll(self):
        query = '''SELECT email, nome, admin FROM public.funcionários'''
        return returnSelect(query, self)
    def selectAllEmail(self):
        query = '''SELECT email FROM public.funcionários'''
        return returnSelect(query, self)
    def checkLogin(self):
        query = '''SELECT 1 FROM public.funcionários WHERE email = %(email)s AND senha = %(senha)s'''
        return returnSelect(query, self)
    def checkAdmin(self):
        query = '''SELECT admin FROM public.funcionários WHERE email = %(email)s'''
        return returnSelect(query, self)
