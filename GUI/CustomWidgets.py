import tkinter as tk
from tkinter import ttk

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
        self.container = scrollFrame(parent)
        canva = self.container.interior
        try:
            rows = len(list)
            columns = len(list[0])
        except IndexError:
            return
        for n in range(len(titles)):
            if n<2 or titles[n]=="Aprovação":
                self.e = myEntry(canva, width=15)
            else:
                self.e = myEntry(canva, width=10)
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
                self.e = myEntry(canva, width=15)
                self.e.grid(row=i + 1, column=columns)
                self.e.insert(tk.END, aprov)
                self.e.configure(state="disabled")
            for j in range(columns):
                if j < 2:
                    self.e = myEntry(canva, width=15)
                else:
                    self.e = myEntry(canva, width=10)
                self.e.grid(row=i+1, column=j)
                self.e.insert(tk.END, list[i][j])
                self.e.configure(state="disabled")
            self.container.pack()

class scrollFrame(ttk.Frame):
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient="vertical")
        vscrollbar.pack(fill="y", side="right", expand=0)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        canvas.pack(side="left", fill="both", expand=1)
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor="nw")

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)