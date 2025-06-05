from tkinter import ttk
import tkinter as tk

from GUI.CustomWidgets import myLabel, myEntry, myButton, Table, scrollFrame
from Objetos.Funcionarios import Funcionario


class adminFuncionario(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        myLabel(self, text="Digite as informações, para remover um funcionario, apenas o email é necessário").pack()
        form = ttk.Frame(self)
        self.email = tk.StringVar(self)
        myLabel(form, text="Email").grid(row=1, column=0)
        myEntry(form, textvariable=self.email).grid(row=1, column=1)
        self.nome = tk.StringVar(self)
        myLabel(form, text="Nome").grid(row=0, column=0)
        myEntry(form, textvariable=self.nome).grid(row=0, column=1)
        self.senha = tk.StringVar(self)
        myLabel(form, text="Senha").grid(row=2, column=0)
        myEntry(form, textvariable=self.senha).grid(row=2, column=1)
        ins = myButton(self, text="Inserir Funcionario", command=self.insert)
        dele = myButton(self, text="Remover Funcionario", command=self.delete)
        self.msgvar = tk.StringVar()
        msgerro = myLabel(self, textvariable=self.msgvar)
        form.pack()
        ins.pack(pady=10)
        dele.pack(pady=10)
        msgerro.pack()
        tabletitle = myLabel(self, "Lista de todas os funcionarios encontradas")
        tabletitle.pack(pady=10)
        self.tablecont = ttk.Frame(self)
        self.tablecont.pack()

    def insert(self):
        tempobj = Funcionario(self.email.get(), self.nome.get(), self.senha.get())
        op = tempobj.insert()
        self.msgvar.set(op)
        self.setup()
    def delete(self):
        tempobj = Funcionario(self.email.get(), self.nome.get(), self.senha.get())
        adm = tempobj.checkAdmin()
        if adm[0][0]:
            self.msgvar.set("Administradores só podem ser alterados pelo banco de dados")
            self.setup()
            return
        op = tempobj.delete()
        self.msgvar.set(op)
        self.setup()
    def setup(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        titles = ["Email", "Nome", "Admin"]
        tempobj = Funcionario(self.email.get(), self.nome.get(), self.senha.get())
        lst = tempobj.selectAll()
        Table(self.tablecont, titles, lst)