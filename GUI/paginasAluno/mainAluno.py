from tkinter import ttk
from GUI.CustomWidgets import myLabel, myButton
from GUI.paginasAluno.inscriçãoAluno import inscricaoAluno
from GUI.paginasAluno.notaAluno import notaAluno


class mainAluno(ttk.Frame):
    def __init__(self, parent, control):
        ttk.Frame.__init__(self, parent)
        self.control = control
        label =myLabel(self, text="Bem vindo ao registro de notas\nQual operação você deseja realizar?")
        label.pack(side="top", fill="x")
        #operações
        options = ttk.Frame(self)
        novainscricao = myButton(options, text="Fazer inscrição",
                           command=lambda: self.showpage("inscricaoAluno"))
        novainscricao.pack(side="left", padx=10, pady=10)
        vernotas = myButton(options, text="Ver suas notas",
                           command=lambda: self.showpage("notaAluno"))
        vernotas.pack(side="left", padx=10, pady=10)
        options.pack()
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        button = myButton(self, text="Sair",
                           command=lambda: control.showpage("mainMenu"))
        button.pack(side="top")
        self.frames={}
        for f in (inscricaoAluno,notaAluno):
            page_name = f.__name__
            frame = f(control=self, parent=container)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.showpage("inscricaoAluno")
    def showpage(self, pagename):
        if pagename == "notaAluno":
            self.frames["notaAluno"].fullTable()
        frame = self.frames[pagename]
        frame.tkraise()