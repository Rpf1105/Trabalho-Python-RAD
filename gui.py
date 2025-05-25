import tkinter as tk
from tkinter import font
from tkinter import ttk


class myApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Banco da escola")
        title = tk.Label(text="Banco de dados magico", font=tk.font.Font(family="Arial", weight="bold"))
        title.pack(side="top")
        #Container que segura as outras paginas
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        #importa classes que definem as paginas em frames e sobrepõe eles
        for f in (mainMenu, mainAluno, pageDisciplinas, pageInscricao):
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
        tk.Frame.__init__(self, parent)
        self.control = control
        label =tk.Label(self, text="Bem vindo ao registro de notas\nQual informação você deseja ver")
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Alunos", command=lambda: control.showpage("mainAluno"))
        button1.pack(pady=10)
        button2 = tk.Button(self, text="Disciplinas", command=lambda: control.showpage("pageDisciplinas"))
        button2.pack(pady=10)
        button3 = tk.Button(self, text="Inscrições", command=lambda: control.showpage("pageInscricao"))
        button3.pack(pady=10)

#aluno
class mainAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        option = tk.StringVar(value="Inserir")
        insert = ["Inserir", "Alterar", "Deletar"]
        select = tk.OptionMenu(self, option, *insert)
        select.pack(side="top")
        changepage = tk.Button(self, text="Enviar",
                           command=lambda: self.showpage("mainMenu"))
        changepage.pack()
        button = tk.Button(self, text="Voltar",
                           command=lambda: control.showpage("mainMenu"))
        button.pack()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for f in (insertAluno, deleteAluno):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showpage("insertAluno")
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()

class insertAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        nome=tk.Entry(self)
        submit = tk.Button(self)
        nome.pack()
        submit.pack()

class deleteAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.controller = control
        label = tk.Label(self, text="delete")
        matricula=tk.Entry(self)
        submit = tk.Button(self)
        label.pack()
        matricula.pack()
        submit.pack()

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