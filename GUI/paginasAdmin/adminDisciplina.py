from tkinter import ttk
import tkinter as tk

from GUI.CustomWidgets import myLabel, myEntry, myButton, Table, scrollFrame
from Objetos.Aluno import Aluno
from Objetos.Disciplina import Disciplina


class adminDisciplina(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        myLabel(self, text="Digite as informações, para remover uma disciplina, apenas o código é necessário").pack()
        form = ttk.Frame(self)
        self.cod = tk.StringVar(self)
        myLabel(form, text="Código").grid(row=1, column=0)
        myEntry(form, textvariable=self.cod).grid(row=1, column=1)
        self.nome = tk.StringVar(self)
        myLabel(form, text="Nome").grid(row=0, column=0)
        myEntry(form, textvariable=self.nome).grid(row=0, column=1)
        self.ano = tk.StringVar(self)
        myLabel(form, text="Ano").grid(row=2, column=0)
        myEntry(form, textvariable=self.ano).grid(row=2, column=1)
        self.sem = tk.StringVar(self)
        myLabel(form, text="Semestre").grid(row=3, column=0)
        myEntry(form, textvariable=self.sem).grid(row=3, column=1)
        ins = myButton(self, text="Inserir Disciplina", command=self.insert)
        dele = myButton(self, text="Remover Disciplina", command=self.delete)
        self.msgvar = tk.StringVar()
        msgerro = myLabel(self, textvariable=self.msgvar)
        form.pack()
        ins.pack(pady=10)
        dele.pack(pady=10)
        msgerro.pack()
        tabletitle = myLabel(self, "Lista de todas as disciplinas encontradas")
        tabletitle.pack(pady=10)
        self.tablecont = ttk.Frame(self)
        self.tablecont.pack()

    def insert(self):
        tempobj = Disciplina(self.nome.get(), self.cod.get(), int(self.ano.get()), int(self.sem.get()))
        op = tempobj.insert()
        self.msgvar.set(op)
        self.setup()
    def delete(self):
        tempobj = Disciplina("",self.cod.get(), 0, 0)
        op = tempobj.delete()
        self.msgvar.set(op)
        self.setup()
    def setup(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        titles = ["Nome", "Código", "Ano", "Semestre"]
        lst = Disciplina.selectAll()
        Table(self.tablecont, titles, lst)
