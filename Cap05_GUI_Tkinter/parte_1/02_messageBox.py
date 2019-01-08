#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
root = Tk()

root.geometry("140x100") # tamanho do da janela


def helloCallBack():
    msg = messagebox.showinfo(title="Hello Python", message="Hello World")


B = Button(root, text="Hello", command=helloCallBack)
B.place(x=50, y=50) # posicionamento do botão
root.mainloop()