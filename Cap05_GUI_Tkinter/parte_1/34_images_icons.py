#!/usr/bin/env python3

from tkinter import *

window = Tk()
window.title("Images and icons")

icon = PhotoImage(file='python_logo.gif')

label = Label(window)
label.config(image=icon)
label.pack()

window.mainloop()