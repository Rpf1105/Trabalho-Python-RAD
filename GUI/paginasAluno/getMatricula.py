import tkinter as tk
from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton, myEntry
from db import connectDb

class getMatricula(ttk.Frame):
    def __init__(self, parent, control):
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
