from tkinter import ttk
import tkinter as tk
from GUI.CustomWidgets import myLabel, myEntry, myButton, Table
from Objetos.Disciplina import Disciplina
from Objetos.Inscrição import Inscricao
from db import connectDb


class inscricaoAluno(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        #pede o código da matéria para inscrição (mudar depois para combobox se der tempo e eu lembrar)
        form = ttk.Frame(self)
        matlabel = myLabel(form, text="Digite o código do curso")
        self.codigo = tk.StringVar()
        cod=myEntry(form, textvariable=self.codigo)
        submit = myButton(self, text="Enviar", command=self.checkDisciplina)
        form.pack()
        matlabel.grid(row=0, column=0)
        cod.grid(row=0, column=1)
        #tabela para mostrar disciplinas existentes
        self.tablecont = ttk.Frame(self)
        submit.pack(pady=10)
        self.msgvar = tk.StringVar(value="")
        mensagem = myLabel(self, textvariable=self.msgvar)
        mensagem.pack()
        self.tablecont.pack()
    def checkDisciplina(self):
        cod = self.codigo.get()
        tempobj = Disciplina("", cod,0,0)
        rows = tempobj.selectNome()
        if rows is None:
            self.msgvar.set("Essa disciplina não existe")
        else:
            #as camadas estão indo fundo demais, pra chegar no cookie da raiz precisa disso, mudar para metodo setup igual o prof
            newinscricao = Inscricao(self.mat, cod)
            newinscricao.insert()
            self.msgvar.set("Inscrição realizada com sucesso")
    def setup(self, cookie):
        self.mat = cookie
        # tabela para mostrar disciplinas existentes
        for child in self.tablecont.winfo_children():
            child.destroy()
        titles = ["Nome", "Código", "Ano", "Semestre"]
        lst = Disciplina.selectAll()
        Table(self.tablecont, titles, lst)
