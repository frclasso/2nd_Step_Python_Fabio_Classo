from tkinter import *
from tkinter import ttk


root = Tk()

frame = Frame(root)

Label(frame, text="A bunch of buttons").pack()


Button(frame, text='B1').pack(side=LEFT, fill=Y)
Button(frame, text='B2').pack(side=TOP, fill=X)
Button(frame, text='B3').pack(side=RIGHT, fill=X)
Button(frame, text='B4').pack(side=LEFT, fill=X)

frame.pack()


root.mainloop()


