import tkinter as tk
from cProfile import label
from tkinter import font, StringVar
from tkinter import ttk

from db import connectDbAluno, queryExec


class myApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Banco da escola")
        header = tk.Frame(self)
        title = tk.Label(header, text="Banco de dados magico",fg="snow",font=tk.font.Font(family="Eras Bold ITC", size=40,))
        title.configure(background="#5864a7")
        header.pack(side="top", expand=True)
        title.pack()
        #Container que segura as outras paginas
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        #importa classes que definem as paginas em frames e sobrepõe eles
        for f in (mainMenu, mainAluno, pageDisciplinas, pageInscricao, getMatricula):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showpage("mainMenu")
    #funcao para trazer um frame pra cima para deixar ele visivel
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()

class mainMenu(tk.Frame):
    def __init__(self, parent, control):
        font = tk.font.Font(family="Arial", size=20)
        tk.Frame.__init__(self, parent)
        self.control = control
        label =tk.Label(self, text="Bem vindo ao registro de notas\nQual desses você é?", font=font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Alunos", command=lambda: control.showpage("getMatricula"),font=font)
        button1.pack(pady=10)
        button2 = tk.Button(self, text="Professor", command=lambda: control.showpage("pageDisciplinas"),font=font)
        button2.pack(pady=10)

class getMatricula(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        tk.Label(self, text="Digite a sua matricula").pack()
        self.matricula = tk.StringVar(self)
        tk.Entry(self, textvariable=self.matricula).pack()
        submit = tk.Button(self, text="Enviar", command=self.checkMatricula)
        submit.pack()
        voltar = tk.Button(self, text="voltar", command=lambda: control.showpage("mainMenu"))
        voltar.pack()
        self.msgvar = tk.StringVar(value="")
        mensagem = tk.Label(self, textvariable=self.msgvar)
        mensagem.pack()
    def checkMatricula(self):
        con = connectDbAluno()
        cursor = con.cursor()
        mat = self.matricula.get()
        cursor.execute('''SELECT * FROM public."Aluno" WHERE "Matricula" = %s;''', (mat,))
        rows = cursor.fetchone()
        if rows is None:
            self.msgvar.set("Essa matricula não existe")
        else:
            self.msgvar.set("")
            self.control.showpage("mainAluno")

#aluno
class mainAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        label =tk.Label(self, text="Bem vindo ao registro de notas\nQual desses você é?")
        label.pack(side="top", fill="x", pady=10)
        novainscricao = tk.Button(self, text="Fazer inscrição",
                           command=lambda: self.showpage("inscricaoAluno"))
        novainscricao.pack()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        button = tk.Button(self, text="Sair",
                           command=lambda: control.showpage("mainMenu"))
        button.pack(side="top")
        self.frames={}
        for f in (inscricaoAluno,):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()

class inscricaoAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        form = tk.Frame()
        matlabel = tk.Label(self, text="Digite o código do curso")
        codigo=tk.Entry(self)
        submit = tk.Button(self, text="Enviar")
        matlabel.grid(row=0, column=0)
        codigo.grid(row=0, column=1)
        submit.grid(row=1, column=0)

#disciplinas
class pageDisciplinas(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        label = tk.Label(self, text="disciplinas")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: control.showpage("mainMenu"))
        button.pack()

class pageInscricao(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        label = tk.Label(self, text="inscricao")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: control.showpage("mainMenu"))
        button.pack()

def init():
    app = myApp()
    app.mainloop()

init()