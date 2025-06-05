from tkinter import ttk
import tkinter as tk

from GUI.CustomWidgets import myLabel, myEntry, myButton, Table, scrollFrame
from Objetos.Aluno import Aluno
from Objetos.Disciplina import Disciplina
from Objetos.Funcionarios import Funcionario
from Objetos.Professor import Professor


class adminDocente(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        myLabel(self, text="Digite as informações para associar ou remover um professor de uma matéria").pack()
        form = ttk.Frame(self)
        self.cod = tk.StringVar(self)
        myLabel(form, text="Código").grid(row=1, column=0)
        self.codbox = ttk.Combobox(form, textvariable=self.cod)
        self.codbox.grid(row=1, column=1)
        self.email = tk.StringVar(self)
        myLabel(form, text="Email").grid(row=0, column=0)
        self.emailbox= ttk.Combobox(form, textvariable=self.email)
        self.emailbox.grid(row=0, column=1)
        ins = myButton(self, text="Associar Professor", command=self.insert)
        dele = myButton(self, text="Remover Professor", command=self.delete)
        self.msgvar = tk.StringVar()
        msgerro = myLabel(self, textvariable=self.msgvar)
        form.pack()
        ins.pack(pady=10)
        dele.pack(pady=10)
        msgerro.pack()
        tabletitle = myLabel(self, "Lista de todas os professores associados")
        tabletitle.pack(pady=10)
        self.tablecont = ttk.Frame(self)
        self.tablecont.pack()

    def insert(self):
        tempobj = Professor(self.email.get(), self.cod.get())
        op = tempobj.insert()
        self.msgvar.set(op)
        self.setup()
    def delete(self):
        tempobj = Professor(self.email.get(),self.cod.get())
        op = tempobj.delete()
        self.msgvar.set(op)
        self.setup()
    def setup(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        titles = ["Email", "Código"]
        tempobj = Professor("","")
        lst = tempobj.selectAll()
        Table(self.tablecont, titles, lst)
        #codigos disciplinas
        tempobj = Disciplina("","",0,0)
        rows=tempobj.selectAllCod()
        self.lst = []
        for cod in rows:
            self.lst.append(cod[0])
        self.codbox["values"] = self.lst
        #email funcionarios
        tempobj = Funcionario("","","")
        rows=tempobj.selectAllEmail()
        self.lst = []
        for cod in rows:
            self.lst.append(cod[0])
        self.emailbox["values"] = self.lst