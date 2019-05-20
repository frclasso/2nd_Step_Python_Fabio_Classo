from tkinter import *
from tkinter import ttk


root = Tk()

frame = Frame(root)

labeText = StringVar()

label = Label(frame, textvariable=labeText)
button = Button(frame, text='Click Me')

labeText.set("I'm a label")

frame.pack()
label.pack()
button.pack()

root.mainloop()


