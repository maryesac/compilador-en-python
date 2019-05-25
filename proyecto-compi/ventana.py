from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class Ventana:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Compilador")
        self.ventana.geometry("1200x600")
        self.ventana.menubar = Menu(self.ventana)
        self.ventana.config(menu=self.ventana.menubar)
        self.ventana.filemenu = Menu(self.ventana.menubar, tearoff = 0)
        self.ventana.filemenu.add_command(label="Abrir")
        self.ventana.filemenu.add_command(label="Guardar Como")
        self.ventana.filemenu.add_separator()
        self.ventana.filemenu.add_command(label="Salir")
        self.ventana.menubar.add_cascade(label="Archivo", menu=self.ventana.filemenu)
        self.ventana.menubar.add_cascade(label="Ejecutar")
        self.textPad = ScrolledText(self.ventana)
        self.textPad.pack()
        self.textPad.place(x=50,y=50)
        self.listbox1 = Listbox(self.ventana, width=45, height=11)
        self.listbox1.pack()
        self.listbox1.place(x=800, y=50)
        self.listbox2 = Listbox(self.ventana, width=45, height=11)
        self.listbox2.pack()
        self.listbox2.place(x=800, y=300)
        self.listbox3 = Listbox(self.ventana, width=82, height=5)
        self.listbox3.pack()
        self.listbox3.place(x=50, y=480)

        #self.textbox = Text(self.ventana, height = 50, width = 79, wrap = 'word')
        #self.textbox.place(x=500, y=500)
        #self.vertscroll = Scrollbar(self.ventana)
        #self.vertscroll.config(command=self.textbox.yview)
        #self.textbox.config(yscrollcommand=self.vertscroll.set)
        #self.textbox.grid(column=0, row=0)
        #self.vertscroll.grid(column=1, row=0, sticky='NS')

        #self.textPad = TextPad(self.ventana, undo=True, maxundo=-1, autoseparators=True)
        #self.textPad.filename = None
        #self.textPad.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        #self.textScrollY = ttk.Scrollbar(self.textPad)
        #self.textScrollY.config(cursor="double_arrow")
        #self.textPad.configure(yscrollcommand=textScrollY.set)
        #self.textScrollY.config(command=self.textPad.yview)
        #self.textScrollY.pack(side=tk.RIGHT, fill=tk.Y)

        #self.var1 = StringVar()
        
        #self.listbox = Listbox(self.ventana, width=80, height=24)

        #self.listbox.pack()
        #self.listbox.place(x=10, y=10)
        #text = Text(self.ventana, width=15,height=15)
        #LB=Text(self.ventana, width=16, height=5)

        #scroll = Scrollbar(self.ventana, command=text.yview)
        #scroll.pack(side=RIGHT, fill=Y)
        #self.label = Entry(self.ventana,textvariable=self.var1,relief="solid",width=100, height=100)
        #self.label.pack()
        #self.var1 = StringVar()
        #self.listbox = Listbox(self.ventana, width=80, height=24)
        #self.listbox = Entry(self.ventana,textvariable=self.var1)
        #self.listbox.pack()
        #self.listbox.place(x=10, y=10)
        #var = StringVar()
        #var.set(self.listbox)
        self.ventana.mainloop()
        # self.raiz = Tk()
        # self.raiz.geometry("800x500")
        # self.automata = Automata(self.raiz)
        # self.entry = Entry(self.raiz,  width=80)
        # self.entry.pack()

        # self.button = Button(self.raiz, text="Validar", command=lambda: self.validador.validar(self.automata,self.entry.get()))
        # self.button.pack()
        # self.raiz.configure(bg = "#e0e0e0")
        # self.raiz.mainloop()
    

if __name__ == "__main__":
    Ventana()