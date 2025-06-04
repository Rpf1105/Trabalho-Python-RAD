from db import queryExec, returnSelect


class Inscricao:
    def __init__(self, aluno, disciplina, sim1=0, sim2=0, av=0, avs=0, nf=0):
        self.aluno = aluno
        self.disciplina = disciplina
        self.sim1 = sim1
        self.sim2 = sim2
        self.av = av
        self.avs = avs
        self.nf = nf
    def insert(self):
        query = '''INSERT INTO public.Inscrição(Aluno,Disciplina) VALUES(%(aluno)s, %(disciplina)s)'''
        return queryExec(query, self)
    def update(self):
        query = '''UPDATE Inscrição SET sim1 = %(sim1)s, sim2=%(sim2)s, av=%(av)s, avs=%(avs)s, nf=%(nf)s WHERE disciplina = %(disciplina)s AND aluno = %(aluno)s'''
        return queryExec(query, self)
    def delete(self):
        query = '''DELETE FROM Inscrição WHERE disciplina = :%(disciplina)s AND aluno = %(aluno)s'''
        return queryExec(query, self)
    def selectAluno(self):
        query = '''SELECT * FROM public.Inscrição WHERE Disciplina = %(disciplina)s AND Aluno = %(aluno)s'''
        return returnSelect(query, self)
    def selectNotas(self):
        query = '''SELECT sim1, sim2, av, avs FROM public.Inscrição WHERE Disciplina = %(disciplina)s AND Aluno = %(aluno)s'''
        return returnSelect(query, self)
    def selectAllAluno(self):
        query = '''SELECT * FROM public.Inscrição WHERE Aluno = %(aluno)s'''
        return returnSelect(query, self)
    def selectAllDisciplina(self):
        query = '''SELECT * FROM public.Inscrição WHERE Disciplina = %(disciplina)s'''
        return returnSelect(query, self)
    def selectAlunoDisciplina(self):
        query = '''SELECT aluno FROM public.Inscrição WHERE Disciplina = %(disciplina)s'''
        return returnSelect(query, self)
