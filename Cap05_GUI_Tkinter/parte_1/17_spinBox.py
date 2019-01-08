#!/usr/bin/env python3

from tkinter import *

root = Tk()

w = Spinbox(root, from_=0, to=10)
w.pack()

root.mainloop()