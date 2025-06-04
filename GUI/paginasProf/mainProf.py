from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton
from GUI.paginasProf.notaProf import notaProf
from GUI.paginasProf.selectProf import selectProf


class mainProf(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        label =myLabel(self, text="Bem vindo ao registro de notas\nQual operação você deseja realizar?")
        label.pack(side="top", fill="x")
        #operações
        options = ttk.Frame(self)
        novainscricao = myButton(options, text="Ver os dados dos seus alunos",
                           command=lambda: self.showpage("selectProf"))
        novainscricao.pack(side="left", padx=5)
        vernotas = myButton(options, text="Inserir as notas",
                           command=lambda: self.showpage("notaProf"))
        vernotas.pack(side="left", padx=5)
        options.pack()
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        button = myButton(self, text="Sair",
                           command=lambda: control.showpage("mainMenu"))
        button.pack(side="top")
        self.frames={}
        for f in (selectProf, notaProf):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    def showpage(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()
    def setup(self):
        self.frames["selectProf"].setup()
        self.frames["notaProf"].setup()