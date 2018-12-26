#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text='Click Me')
button.pack()

# Vamos definir uma função para uma ação do botão
def callback():
    print('Clicked')


button.config(command=callback)

# simulando o clique
button.invoke() # printa 'Clicked'

# desabilitando o botão
button.state(['disabled'])

# para checar se o estado no botão
button.instate(['disabled']) #  retorna True se estiver desabilitado

# para reabilitar
button.state(['!disabled'])


# inserindo uma imagem no botão
logo = PhotoImage(file='python_logo.gif')
button.config(image = logo, compound=LEFT)

# Vamos reduzir o tamanho da logo
small_logo = logo.subsample(5,5)
button.config(image=small_logo)

root.mainloop()