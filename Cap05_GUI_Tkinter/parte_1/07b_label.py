#!/usr/bin/env python3

from tkinter import *

root = Tk()

root.title("Label")

# definindo 3 labels simples contendo texto simples

# sufficient width
Label(root, text = "Sufficient width", fg="white", bg="purple").pack()

# width of x
Label(root, text="Width of x", fg="white", bg="green").pack(fill="x")

# height of y
Label(root, text="Height of y", fg="white", bg='black').pack(side='left', fill='y')

root.mainloop()