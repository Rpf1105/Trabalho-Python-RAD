import tkinter as tk
from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton, myEntry, Table
from Objetos.Aluno import Aluno
from Objetos.Inscrição import Inscricao
from Objetos.Professor import Professor
from db import verifySimNota, verifyAvNota


class notaProf(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        self.tablecont = ttk.Frame(self)
        label = myLabel(self, text="Inserir notas dos alunos")
        label.pack()
        self.formcont = ttk.Frame(self)
        self.mat = tk.StringVar()
        self.cod = tk.StringVar()
        self.nome = tk.StringVar()
        self.sim1 = tk.StringVar()
        self.sim2 = tk.StringVar()
        self.av = tk.StringVar()
        self.avs = tk.StringVar()
        search = ttk.Frame(self)
        codlabel = myLabel(search, text="Escolha o código da matéria registrada")
        self.codentry = ttk.Combobox(search, textvariable=self.cod)
        self.codentry.bind('<<ComboboxSelected>>', self.pesquisarTurma)
        codlabel.grid(row=0, column=0)
        self.codentry.grid(row=0, column=1)
        search.pack()
        self.formcont.pack(pady=30)
        self.msgvar = tk.StringVar()
        msgerro = myLabel(self, textvariable=self.msgvar)
        msgerro.pack()
        self.tablecont.pack()
    def pesquisarTurma(self, event):
        for child in self.formcont.winfo_children():
            child.destroy()
        self.mat.set("")
        self.nome.set("")
        self.sim1.set("")
        self.sim2.set("")
        self.av.set("")
        self.avs.set("")
        if not self.cod.get():
            return self.msgvar.set("Não foi escolhida nenhuma matéria")
        formcont = self.formcont
        form = ttk.Frame(formcont)
        tempobj = Inscricao("", self.cod.get())
        rows = tempobj.selectAlunoDisciplina()
        lst = []
        if not rows:
            return self.msgvar.set("Essa matéria não existe")
        for row in rows:
            lst.append(row[0])
        self.msgvar.set("")
        matlabel = myLabel(form, text="Escolha a matricula do aluno")
        matentry = ttk.Combobox(form, textvariable=self.mat)
        matentry['values'] = lst
        matentry.bind('<<ComboboxSelected>>', self.getNotas)
        labelnome = myLabel(form, text="Nome do Aluno")
        nomeAluno = myEntry(form, textvariable=self.nome, state="readonly")
        sim1label = myLabel(form, text="Sim1")
        sim1entry = myEntry(form, textvariable=self.sim1)
        sim2label = myLabel(form, text="Sim2")
        sim2entry = myEntry(form, textvariable=self.sim2)
        avlabel = myLabel(form, text="Av")
        aventry = myEntry(form, textvariable=self.av)
        avslabel = myLabel(form, text="Avs")
        avsentry = myEntry(form, textvariable=self.avs)
        submit = myButton(formcont, text="Salvar mudanças", command=self.updateNota)
        matlabel.grid(row=0, column=0)
        matentry.grid(row=0, column=1)
        labelnome.grid(row=1, column=0)
        nomeAluno.grid(row=1, column=1)
        sim1label.grid(row=2, column=0)
        sim1entry.grid(row=2, column=1)
        sim2label.grid(row=3, column=0)
        sim2entry.grid(row=3, column=1)
        avlabel.grid(row=4, column=0)
        aventry.grid(row=4, column=1)
        avslabel.grid(row=5, column=0)
        avsentry.grid(row=5, column=1)
        form.pack()
        submit.pack(pady=10)
    def getNotas(self, event):
        mat = self.mat.get()
        cod = self.cod.get()
        tempAluno = Aluno(matricula=mat,nome="")
        nome = tempAluno.selectNome()
        self.nome.set(nome[0][0])
        tempobj = Inscricao(mat,cod)
        rows = tempobj.selectNotas()
        print(rows)
        row = rows[0]
        self.sim1.set(row[0])
        self.sim2.set(row[1])
        self.av.set(row[2])
        self.avs.set(row[3])
    def updateNota(self):
        try:
            sim1 = float(self.sim1.get())
            sim2 = float(self.sim2.get())
            av = float(self.av.get())
            avs = float(self.avs.get())
            verifySimNota(sim1)
        except ValueError:
            self.msgvar.set("Em um ou mais campos foram digitados valores não numericos")
            return
        if not verifySimNota(sim1) or not verifySimNota(sim2):
            self.msgvar.set("A nota dos simulados são invalidas (entre 0 e 1)")
            return
        if not verifyAvNota(av) or not verifyAvNota(avs):
            self.msgvar.set("A nota das avs são invalidas (entre 0 e 10)")
            return
        self.msgvar.set("")
        if av>avs:
            nf = av
        else:
            nf = avs
        nf+= sim1 + sim2
        if nf>10:
            nf=10
        tempobj = Inscricao(aluno=self.mat.get(), disciplina=self.cod.get(), sim1=sim1, sim2=sim2, av=av, avs=avs, nf=nf)
        tempobj.update()
    def setup(self, cookie):
        email = cookie
        tempobj = Professor(email)
        rows=tempobj.selectAllDisciplinas()
        self.lst = []
        for cod in rows:
            self.lst.append(cod[0])
        self.codentry["values"] = self.lst
