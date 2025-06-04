import tkinter as tk
from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton, myEntry
from Objetos.Aluno import Aluno
from db import connectDb

class getMatricula(ttk.Frame):
    def __init__(self, parent, control):
        #Pagina de login para os alunos
        ttk.Frame.__init__(self, parent)
        self.control = control
        myLabel(self, text="Digite a sua matricula").pack()
        self.matricula = tk.StringVar(self)
        myEntry(self, textvariable=self.matricula).pack()
        submit = myButton(self, text="Enviar", command=self.checkMatricula)
        submit.pack(pady=10)
        voltar = myButton(self, text="Voltar", command=lambda: control.showpage("mainMenu"))
        voltar.pack(pady=10)
        self.msgvar = tk.StringVar(value="")
        mensagem = myLabel(self, textvariable=self.msgvar)
        mensagem.pack()
    def checkMatricula(self):
        mat = self.matricula.get()
        tempobj = Aluno("",mat)
        rows = tempobj.selectNome()
        if rows is None:
            self.msgvar.set("Essa matricula não existe")
        else:
            #variavel da janela pai para salvar a matricula do aluno
            self.control.matriculacookie = mat
            self.msgvar.set("")
            self.control.showpage("mainAluno")
