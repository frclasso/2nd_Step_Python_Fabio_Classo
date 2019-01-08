#!/usr/bin/env python3

from tkinter import *

root = Tk()

L1 = Label(root, text="User Name")
L1.pack(side=LEFT)

E1 = Entry(root, bd=5)

E1.pack(side=RIGHT)

root.mainloop()