#!/usr/bin/env python3

from tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=10)
w.pack()

master.mainloop()