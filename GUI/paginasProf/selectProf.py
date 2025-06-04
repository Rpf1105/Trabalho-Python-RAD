import tkinter as tk
from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton, myEntry, Table
from Objetos.Inscrição import Inscricao
from Objetos.Professor import Professor


class selectProf(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        self.tablecont = ttk.Frame(self)
        label = myLabel(self, text="Suas notas")
        label.pack()
        search = ttk.Frame(self)
        self.cod = tk.StringVar()
        codlabel = myLabel(search, text="Escolha o código da matéria")
        self.searchcod = ttk.Combobox(search, textvariable=self.cod)
        self.searchcod.bind('<<ComboboxSelected>>', self.searchTable)
        matlabel = myLabel(search, text="Escolha a matricula")
        self.mat = tk.StringVar()
        self.searchmat = ttk.Combobox(search, textvariable=self.mat)
        self.searchmat.bind('<<ComboboxSelected>>', self.searchAlunoTable)
        reset = myButton(search, text="Redefinir", command=self.fullTable)
        codlabel.pack(side="left")
        self.searchcod.pack(side="left")
        matlabel.pack(side="left")
        self.searchmat.pack(side="left")
        reset.pack(side="left")
        search.pack()
        self.msgvar = tk.StringVar()
        msgerro = myLabel(self, textvariable=self.msgvar)
        msgerro.pack()
        self.tablecont.pack()
    def fullTable(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        self.msgvar.set("")
        self.cod.set("")
        self.mat.set("")
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF", "Aprovação"]
        lst = []
        for mat in self.lst:
            tempobj = Inscricao("", mat)
            lst += tempobj.selectAllDisciplina()
        print(lst)
        Table(self.tablecont, titles, lst, aprovacao=True)
    def searchTable(self, event):
        if self.cod.get() == "":
            self.msgvar.set("Não foi digitado nenhum valor")
            return
        else:
            self.msgvar.set("")
        for child in self.tablecont.winfo_children():
            child.destroy()
        tempobj = Inscricao("", self.cod.get())
        rows = tempobj.selectAlunoDisciplina()
        lst = []
        if not rows:
            return self.msgvar.set("Essa matéria não existe")
        for row in rows:
            lst.append(row[0])
        self.searchmat["values"] = lst
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF", "Aprovação"]
        tempobj = Inscricao("", self.cod.get())
        lst = tempobj.selectAllDisciplina()
        if not lst:
            self.msgvar.set("Nenhuma inscrição foi encontrada, verifique se o código foi digitado corretamente")
            return
        Table(self.tablecont, titles, lst, aprovacao=True)
    def searchAlunoTable(self, event):
        mat = self.mat.get()
        cod = self.cod.get()
        if mat == "":
            self.msgvar.set("Não foi digitado nenhum valor")
            return
        else:
            self.msgvar.set("")
        for child in self.tablecont.winfo_children():
            child.destroy()
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF", "Aprovação"]
        tempobj = Inscricao(self.mat.get(), self.cod.get())
        if cod=="":
            lst = tempobj.selectAllAluno()
        else:
            lst = tempobj.selectAluno()
        if not lst:
            self.msgvar.set("Nenhuma inscrição foi encontrada, verifique se o código foi digitado corretamente")
            return
        Table(self.tablecont, titles, lst, aprovacao=True)
    def setup(self, cookie):
        email = cookie
        tempobj = Professor(email)
        rows=tempobj.selectAllDisciplinas()
        self.lst = []
        for cod in rows:
            self.lst.append(cod[0])
        self.searchcod["values"] = self.lst
        print(self.lst)
        self.fullTable()