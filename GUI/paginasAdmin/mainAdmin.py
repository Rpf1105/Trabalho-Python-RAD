from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton
from GUI.paginasAdmin.adminAluno import adminAluno


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
        vernotas = myButton(options, text="Disciplinas",
                           command=lambda: self.showpage("adminDisciplina"))
        vernotas.pack(side="left", padx=5)
        options.pack()
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        button = myButton(self, text="Sair",
                           command=lambda: control.showpage("mainMenu"))
        button.pack(side="top")
        self.frames={}
        for f in (adminAluno, ):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()
