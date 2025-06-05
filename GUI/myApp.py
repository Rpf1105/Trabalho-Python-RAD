import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from GUI.CustomWidgets import myBigLabel, myLabel, myButton
from GUI.paginasAdmin.adminLogin import adminLogin
from GUI.paginasAdmin.mainAdmin import mainAdmin
from GUI.paginasAluno.mainAluno import mainAluno
from GUI.paginasAluno.getMatricula import getMatricula
from GUI.paginasProf.getLogin import getLogin
from GUI.paginasProf.mainProf import mainProf


class myApp(tb.Window):
    def __init__(self):
        super().__init__(themename="cosmo")
        self.title("Sistema Escolar")
        self.geometry("1280x720")
        header = ttk.Frame(self)
        #essencialmente cookies para manter login, na raiz
        self.matriculacookie = ""
        #cookie de login para caso alguem passe sem se autenticar
        self.logincookie = False
        headercont = ttk.Frame(header)
        logo = myBigLabel(headercont, text="FET")
        name = myLabel(headercont, text="Faculdade Estadual de Tudo")
        header.pack(side="top", expand=True, fill='x')
        headercont.pack(side="top")
        logo.pack(side='left', pady=10, padx=30)
        name.pack(side='left', pady=10)
        #Container que segura as outras paginas
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        #importa classes que definem as paginas em frames e sobrepõe eles
        for f in (mainMenu, mainAluno, getMatricula, getLogin, mainProf, adminLogin, mainAdmin):
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
            self.matriculacookie = ""
            self.logincookie = False
        #passa cookie de login para setup
        if pagename == "mainProf":
            self.frames["mainProf"].setup(self.logincookie)
        if pagename == "mainAluno":
            self.frames["mainAluno"].setup(self.matriculacookie)
        if pagename == "mainAdmin":
            self.frames["mainAdmin"].setup()
        frame.tkraise()

class mainMenu(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        label =myLabel(self, text="Bem vindo ao registro de notas\n     Qual desses você é?      ")
        label.pack(side="top")
        button1 = myButton(self, text="Administrador", command=lambda: control.showpage("adminLogin"))
        button1.pack(pady=10)
        button2 = myButton(self, text="Alunos", command=lambda: control.showpage("getMatricula"))
        button2.pack(pady=10)
        button3 = myButton(self, text="Professor", command=lambda: control.showpage("getLogin"))
        button3.pack(pady=10)