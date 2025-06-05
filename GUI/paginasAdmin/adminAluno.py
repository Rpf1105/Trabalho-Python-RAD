from tkinter import ttk
import tkinter as tk

from GUI.CustomWidgets import myLabel, myEntry, myButton, Table, scrollFrame
from Objetos.Aluno import Aluno


class adminAluno(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        myLabel(self, text="Digite as informações, para adicionar um aluno apenas o nome é necessário,\npara remover um aluno, apenas a matricula é necessária").pack()
        form = ttk.Frame(self)
        self.nome = tk.StringVar(self)
        myLabel(form, text="Nome").grid(row=0, column=0)
        myEntry(form, textvariable=self.nome).grid(row=0, column=1)
        self.mat = tk.StringVar(self)
        myLabel(form, text="Matricula").grid(row=1, column=0)
        myEntry(form, textvariable=self.mat).grid(row=1, column=1)
        ins = myButton(self, text="Inserir Aluno", command=self.insert)
        dele = myButton(self, text="Remover Aluno", command=self.delete)
        self.msgvar = tk.StringVar()
        msgerro = myLabel(self, textvariable=self.msgvar)
        form.pack()
        ins.pack(pady=10)
        dele.pack(pady=10)
        msgerro.pack()
        tabletitle = myLabel(self, "Lista de todos os alunos encontrados")
        tabletitle.pack(pady=10)
        self.tablecont = ttk.Frame(self)
        self.tablecont.pack()

    def insert(self):
        tempobj = Aluno(self.nome.get())
        op = tempobj.insert()
        self.msgvar.set(op)
        self.setup()
    def delete(self):
        tempobj = Aluno("",self.mat.get())
        op = tempobj.delete()
        self.msgvar.set(op)
        self.setup()
    def setup(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        titles = ["Nome", "Matricula"]
        tempobj = Aluno("","")
        lst = tempobj.selectAll()
        Table(self.tablecont, titles, lst)
