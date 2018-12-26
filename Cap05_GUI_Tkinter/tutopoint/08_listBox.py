#!/usr/bin/env python3

from tkinter import *

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "Julia")
Lb1.insert(5, "Djago")
Lb1.insert(6, "Go")


Lb1.pack()
top.mainloop()