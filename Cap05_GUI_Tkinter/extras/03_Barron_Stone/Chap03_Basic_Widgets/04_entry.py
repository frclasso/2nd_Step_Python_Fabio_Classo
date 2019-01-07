#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

root = Tk()
entry = ttk.Entry(root, width=30)
entry.pack()

# capturando a entrada
entry.get() # nao deu certo na IDE

entry.delete(0, 1) # deletando um elemento do inicio
entry.delete(0, END)  # deleta do inicio ao fim

entry.insert(0, 'Enter your password') # insere no inicio
entry.config(show='*')  # substitui os caracteres digitados por '*'

entry.get() # exibe

entry.state(['disabled']) # desabilita a caixa
entry.state(['!disabled']) # reabilita a caixa

entry.state(['readonly']) # somente leitura

root.mainloop()