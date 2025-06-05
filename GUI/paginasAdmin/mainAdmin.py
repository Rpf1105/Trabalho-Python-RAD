from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton
from GUI.paginasAdmin.adminAluno import adminAluno
from GUI.paginasAdmin.adminDisciplina import adminDisciplina
from GUI.paginasAdmin.adminDocente import adminDocente
from GUI.paginasAdmin.adminFuncionario import adminFuncionario
from GUI.paginasAdmin.adminInscrição import adminInscricao


class mainAdmin(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        label =myLabel(self, text="Bem vindo ao registro de notas\nQual operação você deseja realizar?")
        label.pack(side="top", fill="x")
        #operações
        options = ttk.Frame(self)
        alunos = myButton(options, text="Alunos",
                           command=lambda: self.showpage("adminAluno"))
        alunos.pack(side="left", padx=5)
        disciplinas = myButton(options, text="Disciplinas",
                           command=lambda: self.showpage("adminDisciplina"))
        disciplinas.pack(side="left", padx=5)
        inscricao = myButton(options, text="Inscrições",
                           command=lambda: self.showpage("adminInscricao"))
        inscricao.pack(side="left", padx=5)
        funcionario = myButton(options, text="Funcionários",
                               command=lambda: self.showpage("adminFuncionario"))
        funcionario.pack(side="left", padx=5)
        docente = myButton(options, text="Professores",
                             command=lambda: self.showpage("adminDocente"))
        docente.pack(side="left", padx=5)
        options.pack()
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        button = myButton(self, text="Sair",
                           command=lambda: control.showpage("mainMenu"))
        button.pack(side="top")
        self.frames={}
        for f in (adminAluno, adminDisciplina, adminInscricao, adminFuncionario, adminDocente):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()
    def setup(self):
        for f in self.frames.values():
            f.setup()