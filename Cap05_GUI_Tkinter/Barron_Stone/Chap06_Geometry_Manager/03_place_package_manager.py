#!/usr/bin/env python3

# place package manager
from tkinter import *
from tkinter import ttk
root = Tk()

root.geometry('640x480+200+200') # width, height, posicao na tela

#ttk.Label(root, text='Yellow', background='yellow').place(x=100, y=50) # coordenadas absolutas

# os valores para relx e rely são um número fracionario entre 0 e 1
# relx = 0.5 e rely=0.5 , significa manter na metade da janela
# ttk.Label(root, text='Blue', background='blue').place(relx=0.5, rely=0.5) # coordenadas relativas

# No entando qdo diminuimos a janela nao fica exatamente no centro
# para manter o label blue exatamente no centro mesmo redimensionando
# utilizamos a propriedade anchor='center'
# ttk.Label(root, text='Blue', background='blue').place(relx=0.5, rely=0.5, anchor='center')

# Podemos ainda combinar posição relativa e absoluta
# relx=0.5 no meio mais x=100, mais 100 pixels
ttk.Label(root, text='Green', background='green').place(relx=0.5,x=160, rely=0.5, y=50)

# Utilizando índices negativos
ttk.Label(root, text='Orange', background='orange').place(relx=1.0,x=-5,y=5, anchor='ne')
# relx=1.0 totalmente a direita
#x = -5, diminui 5 pixels horizontals, esq para direita
#y = 5 vertical, de cima para baixo 5 pixels
# achor='ne' n=north, e=east superior/direito

# Podemos alterar o tamanho dos labels atraves da propriedade width e height

ttk.Label(root, text='Yellow', background='yellow').place(x=100, y=50, width=100, height=50)

# Podemos ainda tornar os tamanhos dos labels dinâmicos
ttk.Label(root, text='Blue', background='blue').place(relx=0.5, rely=0.5,
                                                      anchor='center', relwidth=0.5, relheight=0.5)
# relwidth=0.5 define o tamanho do para metade da janela pai, dinamicamente


root.mainloop()