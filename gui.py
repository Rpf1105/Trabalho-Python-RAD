import tkinter as tk
from Objetos import *
from cProfile import label
from tkinter import font, StringVar, Label
from tkinter import ttk

from cryptography.fernet import Fernet

import db
from Objetos.Disciplina import Disciplina
from Objetos.Inscrição import Inscricao
from db import connectDb, returnSelect


class myApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Banco da escola")
        header = tk.Frame(self)
        #essencialmente cookies para manter login, na raiz
        self.matriculacookie = tk.StringVar()
        #cookie de login para caso alguem passe sem se autenticar
        self.logincookie = False
        title = tk.Label(self, text="Banco de dados",fg="snow",font=tk.font.Font(family="Eras Bold ITC", size=40,))
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
        for f in (mainMenu, mainAluno, pageDisciplinas, pageInscricao, getMatricula, getLogin, mainProf):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showpage("mainMenu")
    #funcao para trazer um frame pra cima para deixar ele visivel
    def showpage(self, pagename):
        frame = self.frames[pagename]
        if pagename == "mainMenu":
            #apaga dados dos cookies ao voltar ao menu
            self.matriculacookie.set("")
            self.logincookie = False
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
        button2 = tk.Button(self, text="Professor", command=lambda: control.showpage("getLogin"),font=font)
        button2.pack(pady=10)


#aluno
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
        con = connectDb()
        cursor = con.cursor()
        mat = self.matricula.get()
        cursor.execute('''SELECT * FROM public.Aluno WHERE Matricula = %s;''', (mat,))
        rows = cursor.fetchone()
        if rows is None:
            self.msgvar.set("Essa matricula não existe")
        else:
            #variavel da janela pai para salvar a matricula do aluno
            self.control.matriculacookie.set(mat)
            self.msgvar.set("")
            self.control.showpage("mainAluno")


class mainAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        label =tk.Label(self, text="Bem vindo ao registro de notas\nQual operação você deseja realizar?")
        label.pack(side="top", fill="x", pady=10)
        #operações
        options = tk.Frame(self)
        novainscricao = tk.Button(options, text="Fazer inscrição",
                           command=lambda: self.showpage("inscricaoAluno"),padx=5)
        novainscricao.pack(side="left")
        vernotas = tk.Button(options, text="Ver suas notas",
                           command=lambda: self.showpage("notaAluno"), padx=5)
        vernotas.pack(side="left")
        options.pack()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        button = tk.Button(self, text="Sair",
                           command=lambda: control.showpage("mainMenu"))
        button.pack(side="top")
        self.frames={}
        for f in (inscricaoAluno,notaAluno):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.showpage("inscricaoAluno")
    def showpage(self, pagename):
        if pagename == "notaAluno":
            self.frames["notaAluno"].fullTable()
        frame = self.frames[pagename]
        frame.tkraise()

class inscricaoAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        form = tk.Frame(self)
        matlabel = tk.Label(form, text="Digite o código do curso")
        self.codigo = tk.StringVar(self)
        codigo=tk.Entry(form, textvariable=self.codigo)
        submit = tk.Button(self, text="Enviar", command=self.checkDisciplina)
        form.pack(pady=10)
        matlabel.grid(row=0, column=0)
        codigo.grid(row=0, column=1)
        #tabela para mostrar disciplinas existentes
        titles = ["Nome", "Código", "Ano", "Semestre"]
        tablecont = tk.Frame(self, padx=20, pady=20)
        Table(tablecont, titles, Disciplina.selectAll(connectDb()))
        submit.pack()
        self.msgvar = tk.StringVar(value="")
        mensagem = tk.Label(self, textvariable=self.msgvar)
        mensagem.pack()
        tablecont.pack()
    def checkDisciplina(self):
        con = connectDb()
        cursor = con.cursor()
        cod = self.codigo.get()
        cursor.execute('''SELECT * FROM public.Disciplina WHERE Código = %s;''', (cod,))
        rows = cursor.fetchone()
        if rows is None:
            self.msgvar.set("Essa disciplina não existe")
        else:
            #as camadas estão indo fundo demais, pra chegar no cookie da raiz precisa disso
            self.msgvar.set("")
            newinscricao = Inscricao(self.control.control.matriculacookie.get(), cod)
            newinscricao.insert(connectDb())

class notaAluno(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        self.tablecont = tk.Frame(self, padx=20)
        label = tk.Label(self, text="Suas notas")
        label.pack()
        search = tk.Frame(self)
        self.cod = tk.StringVar()
        entrylabel = tk.Label(search, text="Digite o código da matéria registrada")
        searchbar = tk.Entry(search, textvariable=self.cod)
        submit = tk.Button(search, text="Pesquisar", command=self.searchTable)
        reset = tk.Button(search, text="Redefinir", command=self.fullTable)
        entrylabel.pack(side="left")
        searchbar.pack(side="left")
        submit.pack(side="left")
        reset.pack(side="left")
        search.pack()
        self.msgvar = tk.StringVar()
        msgerro = tk.Label(self, textvariable=self.msgvar)
        msgerro.pack()
        self.tablecont.pack()

    def fullTable(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        self.msgvar.set("")
        matricula = self.control.control.matriculacookie.get()
        print(matricula)
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF"]
        tempobj = Inscricao(matricula, "")
        lst = tempobj.selectAllAluno(connectDb())
        Table(self.tablecont, titles, lst)

    def searchTable(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        if self.cod.get() == "":
            self.msgvar.set("Não foi digitado nenhum valor")
            return
        else:
            self.msgvar.set("")
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF"]
        tempobj = Inscricao(self.control.control.matriculacookie.get(), self.cod.get())
        lst = tempobj.select(connectDb())
        if not lst:
            self.msgvar.set("Nenhuma inscrição foi encontrada, verifique se o código foi digitado corretamente")
            return
        Table(self.tablecont, titles, lst)


#professor
class getLogin(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        tk.Label(self, text="Digite as suas credenciais").pack()
        form = tk.Frame(self)
        self.email = tk.StringVar(self)
        tk.Label(form, text="Usuario").grid(row=0, column=0)
        tk.Entry(form, textvariable=self.email).grid(row=0, column=1)
        self.password = tk.StringVar(self)
        tk.Label(form, text="Senha").grid(row=1, column=0)
        tk.Entry(form, textvariable=self.password).grid(row=1, column=1)
        submit = tk.Button(self, text="Enviar", command=self.checkLogin)
        form.pack()
        submit.pack()
        voltar = tk.Button(self, text="voltar", command=lambda: control.showpage("mainMenu"))
        voltar.pack()
        self.msgvar = tk.StringVar(value="")
        mensagem = tk.Label(self, textvariable=self.msgvar)
        mensagem.pack()
    def checkLogin(self):
        user = self.email.get()
        password = self.password.get()
        query = '''SELECT 1 FROM public.funcionários WHERE email = %s AND senha = %s'''
        rows = returnSelect(connectDb(), query, (user, password))
        print(rows)
        if not rows :
            self.msgvar.set("O usuario e/ou senha estão incorretos")
        else:
            #variavel da janela pai para salvar a matricula do aluno
            self.control.logincookie = True
            self.msgvar.set("")
            self.control.showpage("mainProf")

class mainProf(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        label =tk.Label(self, text="Bem vindo ao registro de notas\nQual operação você deseja realizar?")
        label.pack(side="top", fill="x", pady=10)
        #operações
        options = tk.Frame(self)
        novainscricao = tk.Button(options, text="Ver os dados dos seus alunos",
                           command=lambda: self.showpage("profDados"),padx=5)
        novainscricao.pack(side="left")
        vernotas = tk.Button(options, text="Inserir as notas",
                           command=lambda: self.showpage("notaProf"), padx=5)
        vernotas.pack(side="left")
        options.pack()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        button = tk.Button(self, text="Sair",
                           command=lambda: control.showpage("mainMenu"))
        button.pack(side="top")
        self.frames={}
        for f in (notaProf,):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()

class notaProf(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        self.tablecont = tk.Frame(self)
        label = tk.Label(self, text="Suas notas")
        label.pack()
        search = tk.Frame(self)
        self.cod = tk.StringVar()
        entrylabel = tk.Label(search, text="Digite o código da matéria registrada")
        searchbar = tk.Entry(search, textvariable=self.cod)
        submit = tk.Button(search, text="Pesquisar", command=self.searchTable)
        reset = tk.Button(search, text="Redefinir", command=self.fullTable)
        entrylabel.pack(side="left")
        searchbar.pack(side="left")
        submit.pack(side="left")
        reset.pack(side="left")
        search.pack()
        self.msgvar = tk.StringVar()
        msgerro = tk.Label(self, textvariable=self.msgvar)
        msgerro.pack()
        self.tablecont.pack()
    def fullTable(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        self.msgvar.set("")
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF"]
        tempobj = Inscricao(self.control.control.matriculacookie.get(), "")
        lst = tempobj.selectAllAluno(connectDb())
        Table(self.tablecont, titles, lst)

    def searchTable(self):
        if self.cod.get() == "":
            self.msgvar.set("Não foi digitado nenhum valor")
            return
        else:
            self.msgvar.set("")
        for child in self.tablecont.winfo_children():
            child.destroy()
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF"]
        tempobj = Inscricao(self.control.control.matriculacookie.get(), self.cod.get())
        lst = tempobj.select(connectDb())
        if not lst:
            self.msgvar.set("Nenhuma inscrição foi encontrada, verifique se o código foi digitado corretamente")
            return
        Table(self.tablecont, titles, lst)

class pageDisciplinas(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        label = tk.Label(self, text="disciplinas")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: control.showpage("mainMenu"))
        button.pack()

class pageInscricao(tk.Frame):
    def __init__(self, parent, control):
        tk.Frame.__init__(self, parent)
        self.control = control
        label = tk.Label(self, text="inscricao")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar",
                           command=lambda: control.showpage("mainMenu"))
        button.pack()
# gerador de tabelas
class Table:
    def __init__(self, parent, titles, list):
        try:
            rows = len(list)
            columns = len(list[0])
        except IndexError:
            return
        for n in range(len(titles)):
            self.e = tk.Entry(parent, width=20,
                           font=('Arial', 12, 'bold'))
            self.e.grid(row=0, column=n)
            self.e.insert(tk.END, titles[n])
            self.e.configure(state="disabled")
        for i in range(rows):
            for j in range(columns):
                self.e = tk.Entry(parent, width=20,
                               font=('Arial', 12))

                self.e.grid(row=i+1, column=j)
                self.e.insert(tk.END, list[i][j])
                self.e.configure(state="disabled")
def init():
    app = myApp()
    app.mainloop()

init()