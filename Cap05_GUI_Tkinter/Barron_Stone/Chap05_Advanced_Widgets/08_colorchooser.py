#!/usr/bin/env python3

from tkinter import *
from tkinter.colorchooser import askcolor
root = Tk()


def setBGColor():
    (triple, hexstr) = askcolor()
    if hexstr:
        print(hexstr)
        push.config(bg=hexstr)


push = Button(root, text='Set Background Color', command=setBGColor)
push.config(height=3, font=('Times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)

root.mainloop()
