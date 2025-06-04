from tkinter import ttk
import tkinter as tk
from GUI.CustomWidgets import myLabel, myEntry, myButton, Table
from Objetos.Inscrição import Inscricao


class notaAluno(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        self.tablecont = ttk.Frame(self)
        label = myLabel(self, text="Suas notas")
        label.pack()
        search = ttk.Frame(self)
        self.cod = tk.StringVar()
        entrylabel = myLabel(search, text="Digite o código da matéria registrada")
        searchbar = myEntry(search, textvariable=self.cod)
        submit = myButton(search, text="Pesquisar", command=self.searchTable)
        reset = myButton(search, text="Redefinir", command=self.fullTable)
        entrylabel.pack(side="left")
        searchbar.pack(side="left")
        submit.pack(side="left")
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
        matricula = self.control.control.matriculacookie.get()
        print(matricula)
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF", "Aprovação"]
        tempobj = Inscricao(matricula, "")
        lst = tempobj.selectAllAluno()
        Table(self.tablecont, titles, lst, aprovacao=True)

    def searchTable(self):
        for child in self.tablecont.winfo_children():
            child.destroy()
        if self.cod.get() == "":
            self.msgvar.set("Não foi digitado nenhum valor")
            return
        else:
            self.msgvar.set("")
        titles = ["Matricula", "Código", "Sim 1", "Sim 2", "Av", "Avs", "NF", "Aprovação"]
        tempobj = Inscricao(self.control.control.matriculacookie.get(), self.cod.get())
        lst = tempobj.selectAluno()
        if not lst:
            self.msgvar.set("Nenhuma inscrição foi encontrada, verifique se o código foi digitado corretamente")
            return
        Table(self.tablecont, titles, lst, aprovacao=True)