from tkinter import ttk
import tkinter as tk

from GUI.CustomWidgets import myLabel, myEntry, myButton, Table, scrollFrame
from Objetos.Aluno import Aluno
from Objetos.Disciplina import Disciplina
from Objetos.Inscrição import Inscricao


class adminInscricao(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        myLabel(self, text="Digite a matricula e o código da inscrição a ser removida\n").pack()
        form = ttk.Frame(self)
        self.cod = tk.StringVar(self)
        myLabel(form, text="Código").grid(row=1, column=0)
        myEntry(form, textvariable=self.cod).grid(row=1, column=1)
        self.mat = tk.StringVar(self)
        myLabel(form, text="Matricula").grid(row=0, column=0)
        myEntry(form, textvariable=self.mat).grid(row=0, column=1)
        dele = myButton(self, text="Remover Inscrição", command=self.delete)
        self.msgvar = tk.StringVar()
        msgerro = myLabel(self, textvariable=self.msgvar)
        form.pack()
        dele.pack(pady=10)
        msgerro.pack()
        tabletitle = myLabel(self, "Lista de todas as inscrições encontradas")
        tabletitle.pack(pady=10)
        self.tablecont = ttk.Frame(self)
        self.tablecont.pack(fill="x")

    def delete(self):
        tempobj = Inscricao(self.mat.get(),self.cod.get())
        op = tempobj.delete()
        self.msgvar.set(op)
        self.setup()
    def setup(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF", "Aprovação"]
        tempobj = Inscricao("", "")
        lst = tempobj.selectAll()
        Table(self.tablecont, titles, lst, aprovacao=True)
