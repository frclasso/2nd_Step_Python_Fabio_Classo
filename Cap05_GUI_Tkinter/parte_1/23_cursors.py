#!/usr/bin/env python3

from tkinter import *

root = Tk()

B1 = Button(root, text='circle', relief=RAISED, cursor='circle')
B2 = Button(root, text='plus', relief=RAISED, cursor='plus')

B1.pack()
B2.pack()

root.mainloop()