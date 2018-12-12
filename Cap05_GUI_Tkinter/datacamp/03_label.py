#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()

window.title("Label")

# definindo 3 labels simples contendo texto simples

# sufficient width
tkinter.Label(window, text = "Sufficient width", fg="white", bg="purple").pack()

# width of x

tkinter.Label(window, text="Width of x", fg="white", bg="green").pack(fill="x")

# height of y

tkinter.Label(window, text="Height of y", fg="white", bg='black').pack(side='left', fill='y')

window.mainloop()