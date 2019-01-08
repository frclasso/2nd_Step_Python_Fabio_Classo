#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry("140x100") # tamanhdo da janela


def helloCallBack():
    msg = messagebox.showinfo(title="Hello Pyton", message="Hello World")


B = Button(top, text="Hello", command=helloCallBack)
B.place(x=50, y=50) # posicionamento do botão
top.mainloop()