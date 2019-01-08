#!/usr/bin/env python3

from tkinter import *

root = Tk()

Lb1 = Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "Julia")
Lb1.insert(5, "Django")
Lb1.insert(6, "Go")


Lb1.pack()
root.mainloop()