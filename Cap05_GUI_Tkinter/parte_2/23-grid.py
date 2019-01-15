#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

root = Tk()

# Usando grid package manager não precisamos nos preocupar com a ordem
# definimos o posicionamento dos objetos utilizando rows e columns
# ttk.Label(root, text="Yellow", background='yellow').grid(row=1, column=1)
# ttk.Label(root, text="Blue", background='blue').grid(row=1, column=0 )
# ttk.Label(root, text="Green", background='green').grid(row=0, column=0)
# ttk.Label(root, text="Orange", background='orange').grid(row=0, column=1)


# Alterando largura e altura atraves de columnspan e rowspan
# ttk.Label(root, text="Yellow",
#           background='yellow').grid(row=0, column=2, rowspan=2)
#
# ttk.Label(root, text="Blue",
#           background='blue').grid(row=1, column=0, columnspan=2)
#
# ttk.Label(root, text="Green", background='green').grid(row=0, column=0)
# ttk.Label(root, text="Orange", background='orange').grid(row=0, column=1)

# Utilizamos a propriedade stick para posicionar dentro da celulda
# e(est) direita, w(west) esquerda, n(north) superior e s(south) inferior
# ttk.Label(root, text="Yellow",
#           background='yellow').grid(row=0, column=2, rowspan=2)
#
# ttk.Label(root, text="Blue",
#           background='blue').grid(row=1, column=0, columnspan=2, stick='e')
#
# ttk.Label(root, text="Green", background='green').grid(row=0, column=0)
# ttk.Label(root, text="Orange", background='orange').grid(row=0, column=1)


# aplicando stick nsew
# ttk.Label(root, text="Yellow",
#           background='yellow').grid(row=0, column=2, rowspan=2, stick='nsew')
#
# ttk.Label(root, text="Blue",
#           background='blue').grid(row=1, column=0, columnspan=2, stick='nsew')
#
# ttk.Label(root, text="Green", background='green').grid(row=0, column=0, stick='nsew')
# ttk.Label(root, text="Orange", background='orange').grid(row=0, column=1, stick='nsew')


# A propriede stick='nsew' nao redimensiona o label quando redimensionamos o widget pai(root)
# Para isso utilizamos a propriedade weight

# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=3) # row 1 expande 3x o valor de row 0 em pixels
#
# # alterando o weigth das colunas
# root.columnconfigure(2, weight=1)
#
# ttk.Label(root, text="Yellow",
#           background='yellow').grid(row=0, column=2, rowspan=2, stick='nsew')
#
# ttk.Label(root, text="Blue",
#           background='blue').grid(row=1, column=0, columnspan=2, stick='nsew')
#
# ttk.Label(root, text="Green", background='green').grid(row=0, column=0, stick='nsew')
# ttk.Label(root, text="Orange", background='orange').grid(row=0, column=1, stick='nsew')


# Adicionando padding interno e externo aos labels

ttk.Label(root, text="Yellow",
          background='yellow').grid(row=0, column=2, rowspan=2, stick='nsew')

ttk.Label(root, text="Blue",
          background='blue').grid(row=1, column=0, columnspan=2, stick='nsew')

ttk.Label(root, text="Green", background='green').grid(row=0, column=0, stick='nsew',
                                                       padx=10, pady=10)#padding externo

ttk.Label(root, text="Orange", background='orange').grid(row=0, column=1, stick='nsew',
                                                         ipadx=25, ipady=25) # padding interno

root.mainloop()