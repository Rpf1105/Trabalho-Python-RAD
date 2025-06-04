import tkinter as tk

class myEntry(tk.Entry):
    def __init__(self, parent, textvariable=None, state="normal", width=30):
        font = tk.font.Font(family="Arial", size=15)
        tk.Entry.__init__(self, master=parent ,font=font, textvariable=textvariable, state=state, width=width)

class myBigLabel(tk.Label):
    def __init__(self, parent, text):
        font = tk.font.Font(family="Arial", size=40)
        tk.Label.__init__(self, master=parent ,font=font, text=text)

class myLabel(tk.Label):
    def __init__(self, parent, text=None, textvariable=None):
        font = tk.font.Font(family="Arial", size=15)
        tk.Label.__init__(self, master=parent ,font=font, text=text, textvariable=textvariable)

class myButton(tk.Button):
    def __init__(self, parent, command,text=None):
        font = tk.font.Font(family="Arial", size=15)
        tk.Button.__init__(self, master=parent, command=command, font=font, text=text, pady=10, padx=10)

class Table:
    def __init__(self, parent, titles, list, aprovacao=False):
        try:
            rows = len(list)
            columns = len(list[0])
        except IndexError:
            return
        for n in range(len(titles)):
            self.e = myEntry(parent, width=15)
            self.e.grid(row=0, column=n)
            self.e.insert(tk.END, titles[n])
            self.e.configure(state="disabled")
        for i in range(rows):
            if aprovacao:
                nf = list[i][columns - 1]
                if nf>=6:
                    aprov = "Aprovado"
                else:
                    aprov = "Reprovado"
                self.e = myEntry(parent, width=15)
                self.e.grid(row=i + 1, column=columns)
                self.e.insert(tk.END, aprov)
                self.e.configure(state="disabled")
            for j in range(columns):
                self.e = myEntry(parent, width=15)
                self.e.grid(row=i+1, column=j)
                self.e.insert(tk.END, list[i][j])
                self.e.configure(state="disabled")