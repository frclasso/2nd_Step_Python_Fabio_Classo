#!/usr/bin/env python3

from tkinter import *

window = Tk()
window.title("Images and icons")

icon = PhotoImage(file='python_logo.png') # tkinter.TclError: couldn't recognize data in image file "haha.png"
#displaying the picture usina a 'Label'
label = Label(window, image=icon)
label.pack()

window.mainloop()