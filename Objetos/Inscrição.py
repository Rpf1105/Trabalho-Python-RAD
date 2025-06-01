from db import queryExec, connectDb, returnSelect


class Inscricao:
    def __init__(self, aluno, disciplina):
        self.aluno = aluno
        self.disciplina = disciplina
        self.sim1 = ""
        self.sim2 = ""
        self.av = ""
        self.avs = ""
    def insert(self):
        query = '''INSERT INTO public.Inscrição(Aluno,Disciplina) VALUES(%(aluno)s, %(disciplina)s)'''
        return queryExec(connectDb(), query, self)
    def update(self):
        self.avescolha = input("Digite o nome da av a registrar a nota (sim1, sim2, av, avs): ").lower()
        query = '''UPDATE Inscrição SET :avescolha = :nota WHERE disciplina = :disciplina AND aluno = :aluno'''
        return queryExec(connectDb(), query, self)
    def delete(self):
        query = '''DELETE FROM Inscrição WHERE disciplina = :disciplina AND aluno = :aluno'''
        return queryExec(connectDb(), query, self)
    def select(self):
        query = '''SELECT * FROM public.Inscrição WHERE Disciplina = %(disciplina)s AND Aluno = %(aluno)s'''
        return returnSelect(connectDb(), query, self)
    def selectAllAluno(self):
        query = '''SELECT * FROM public.Inscrição WHERE Aluno = %(aluno)s'''
        return returnSelect(connectDb(), query, self)
    def selectAllDisciplina(self):
        query = '''SELECT * FROM public.Inscrição WHERE "Disciplina" = %(disciplina)s'''
        return returnSelect(connectDb(), query, self)
