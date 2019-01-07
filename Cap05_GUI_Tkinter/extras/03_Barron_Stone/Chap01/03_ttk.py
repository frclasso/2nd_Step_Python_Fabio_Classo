#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

'''Se não der certo na IDE, rodar no terminal'''

root = Tk()  # cria a janela de mais alto nível
button = ttk.Button(root, text='Click Me!')
button.pack()  # carregas as informações na janela principal

button['text']  # Retorna o valor contido na janela
button['text'] = 'Press Me' # altera o valor
button.config(text='Click Me again!')
button.config() # imprime as funções disponíveis, semelhante ao dir()

# add novo Label

ttk.Label(root, text='Hello, Tkinter').pack()

root.mainloop()