#!/usr/bin/env python3

from tkinter import  *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text='Red', fg='red')
redbutton.pack(side=LEFT)

brownbutton = Button(frame, text='Brown', fg='brown')
brownbutton.pack(side=LEFT)

bluebutton = Button(frame, text='Blue', fg='blue')
bluebutton.pack(side=LEFT)


blackbutton = Button(frame, text='Black', fg='black')
blackbutton.pack(side=BOTTOM)


root.mainloop()

