#!/usr/bin/env python3

from tkinter import *

root = Tk()

# renomeando o título da janela
root.title('Interface GUI')

# a função pack é utilizada para exibir o objeto na janela

label= Label(root, text="Hello  Tkinter World!!!").pack()

root.mainloop()