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
        form = ttk.Frame(self)
        matlabel = myLabel(form, text="Digite o código do curso")
        self.codigo = tk.StringVar()
        cod=myEntry(form, textvariable=self.codigo)
        submit = myButton(self, text="Enviar", command=self.checkDisciplina)
        form.pack()
        matlabel.grid(row=0, column=0)
        cod.grid(row=0, column=1)
        #tabela para mostrar disciplinas existentes
        titles = ["Nome", "Código", "Ano", "Semestre"]
        tablecont = ttk.Frame(self)
        Table(tablecont, titles, Disciplina.selectAll())
        submit.pack(pady=10)
        self.msgvar = tk.StringVar(value="")
        mensagem = myLabel(self, textvariable=self.msgvar)
        mensagem.pack()
        tablecont.pack()
    def checkDisciplina(self):
        con = connectDb()
        cursor = con.cursor()
        cod = self.codigo.get()
        cursor.execute('''SELECT * FROM public.Disciplina WHERE Código = %s;''', (cod,))
        rows = cursor.fetchone()
        if rows is None:
            self.msgvar.set("Essa disciplina não existe")
        else:
            #as camadas estão indo fundo demais, pra chegar no cookie da raiz precisa disso
            newinscricao = Inscricao(self.control.control.matriculacookie.get(), cod)
            newinscricao.insert()
            self.msgvar.set("Inscrição realizada com sucesso")
