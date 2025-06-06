import tkinter as tk
from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton, myEntry
from Objetos.Funcionarios import Funcionario


class mudarSenha(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        form = ttk.Frame(self)
        self.senha1 = tk.StringVar(self)
        myLabel(form, text="Senha").grid(row=0, column=0)
        myEntry(form, textvariable=self.senha1).grid(row=0, column=1)
        self.senha2 = tk.StringVar(self)
        myLabel(form, text="Confirmar Senha").grid(row=1, column=0)
        myEntry(form, textvariable=self.senha2).grid(row=1, column=1)
        submit = myButton(self, text="Enviar", command=self.changePass)
        form.pack()
        submit.pack(pady=10)
        self.msgvar = tk.StringVar(value="")
        mensagem = myLabel(self, textvariable=self.msgvar)
        mensagem.pack()
    def changePass(self):
        senha1 = self.senha1.get()
        senha2 = self.senha2.get()
        email = self.email
        if senha1 != senha2:
            self.msgvar.set("As senhas são diferentes")
            return
        tempobj = Funcionario(email, senha1)
        msg = tempobj.updatePass()
        self.msgvar.set(msg)

    def setup(self, cookie):
        self.email = cookie