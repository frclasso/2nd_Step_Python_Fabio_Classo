#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()

# renomeando o título da janela
window.title('Interface GUI')

# a função pack é utilizada para exibir o objeto na janela

label= tkinter.Label(window, text="Hello  Tkinter World!!!").pack()

window.mainloop()