#!/usr/bin/env python3

from tkinter import *

root = Tk()

root.title("Grid")

# creating two input text labels  and input labels
Label(root, text="Username").grid(row=0)  # posicionado em 0 0
# a função Entry é usada para exibir o campo de entrada
Entry(root).grid(row=0, column=1) # posicionado em 0 1

Label(root, text="PASSWORD").grid(row=1) # posicionado em 1 0
Entry(root).grid(row=1, column=1) # posicionado em 1 1

# a função ChekcButtom é usada para criar check buttons
Checkbutton(root, text="Keep Me Logged In").grid(columnspan=2)
# columnspam define a largura de duas colunas é possível usar rowspan da mesma maneira

root.mainloop()