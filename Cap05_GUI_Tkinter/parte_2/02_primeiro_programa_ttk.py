#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk


root = Tk()
button = ttk.Button(root, text='Click Me!')
button.pack()

# button['text']  # Retorna o valor contido na janela
# button['text'] = 'Press Me' # altera o valor

#button.config(text='Click Me again!')
print(button.config()) # imprime as funções disponíveis, semelhante ao dir()

# add novo Label

ttk.Label(root, text='Hello, Tkinter').pack()

root.mainloop()