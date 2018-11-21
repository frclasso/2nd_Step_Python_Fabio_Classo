#!/usr/bin/env python3

from tkinter import *

root = Tk()

b=0
for r in range(6):
    for c in range(6):
        b +=1
        Button(root, text=str(b),borderwidth=1).grid(row=r, column=c)

root.mainloop()