import tkinter as tk
from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton, myEntry
from Objetos.Funcionarios import Funcionario


class adminLogin(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        myLabel(self, text="Digite as suas credenciais").pack()
        form = ttk.Frame(self)
        self.email = tk.StringVar(self)
        myLabel(form, text="Email").grid(row=0, column=0)
        myEntry(form, textvariable=self.email).grid(row=0, column=1)
        self.password = tk.StringVar(self)
        myLabel(form, text="Senha").grid(row=1, column=0)
        myEntry(form, textvariable=self.password).grid(row=1, column=1)
        submit = myButton(self, text="Enviar", command=self.checkLogin)
        form.pack()
        submit.pack(pady=10)
        voltar = myButton(self, text="Voltar", command=lambda: control.showpage("mainMenu"))
        voltar.pack(pady=10)
        self.msgvar = tk.StringVar(value="")
        mensagem = myLabel(self, textvariable=self.msgvar)
        mensagem.pack()
    def checkLogin(self):
        user = self.email.get()
        password = self.password.get()
        tempobj = Funcionario(user, password)
        rows = tempobj.checkLogin()
        print(rows)
        if not rows :
            self.msgvar.set("O usuário e/ou senha estão incorretos")
        else:
            rows = tempobj.checkAdmin()
            if rows[0][0] is True:
                self.control.logincookie = user
                self.msgvar.set("")
                self.control.showpage("mainAdmin")
            else:
                self.msgvar.set("Você não tem permissão de acesso")