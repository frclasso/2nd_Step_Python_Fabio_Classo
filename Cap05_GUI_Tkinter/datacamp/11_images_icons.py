#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()
window.title("Images and icons")

icon = tkinter.PhotoImage(file='haha.png') # tkinter.TclError: couldn't recognize data in image file "haha.png"
#displaying the picture usina a 'Label'
label = tkinter.Label(window, image=icon)
label.pack()

window.mainloop()