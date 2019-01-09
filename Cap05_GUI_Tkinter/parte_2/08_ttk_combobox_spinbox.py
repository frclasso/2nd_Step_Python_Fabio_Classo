#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

root = Tk()

# combobox usando ttk modulo
month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.pack() # até aqui temos uma janela sem os meses

# passando valores para a comboox, inserindo uma tupla de meses
combobox.config(values=('Jan', 'Fev', 'Mar', 'Apr','May', 'Jun', 'Jul',
                        'Aug', 'Oct', 'Nov', 'Dez'))

print(month.get())  # nao funciona
month.set('Jan')  # define o mês


# SpinBox, usando tkinter original, não ttk
year = StringVar()
Spinbox(root, from_=1990, to=2018, textvariable=year).pack()
year.set(2018)

root.mainloop()