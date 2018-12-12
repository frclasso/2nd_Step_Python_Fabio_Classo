#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()

window.title("Grid")

# creating two input text labels  and input labels

tkinter.Label(window, text="Username").grid(row = 0)  # posicionado em 0 0
# a função Entry é usada para exibir o campo de entrada
tkinter.Entry(window).grid(row=0, column=1) #posicionado em 0 1

tkinter.Label(window, text="PASSWORD").grid(row=1) # posicionado em 1 0
tkinter.Entry(window).grid(row=1, column=1) # posicionaodm em 1 1

# a função ChekcButtom é usada para criar chekc buttons
tkinter.Checkbutton(window, text="Keep Me Logged In").grid(columnspan=2)

# columnspam define a largura de duas colunas é possível usar rowspan da mesma maneira

window.mainloop()