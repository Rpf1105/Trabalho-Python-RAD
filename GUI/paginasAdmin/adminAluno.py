from tkinter import ttk
import tkinter as tk

from GUI.CustomWidgets import myLabel, myEntry, myButton
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
        form.pack()
        ins.pack(pady=10)
        dele.pack(pady=10)
    def insert(self):
        tempobj = Aluno(self.nome.get())
        tempobj.insert()
    def delete(self):
        tempobj = Aluno("",self.mat.get())
        tempobj.delete()


