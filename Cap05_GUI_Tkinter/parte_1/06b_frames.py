#!/usr/bin/env python3


from tkinter import *

root = Tk()

root.title('Frame')

# criando 2 frames um TOP e outro BOTTOM

top_frame = Frame(root).pack()
bottom_frame = Frame(root).pack(side="bottom")

# criando widgets para os frames top e bottom

btn1 = Button(top_frame, text="Button 1", fg="red").pack()
btn2 = Button(top_frame, text="Button 2", fg="green").pack()
btn3 = Button(bottom_frame, text="Button 3", fg="purple").pack(side='left')
btn4 = Button(bottom_frame, text="Button 4", fg="blue").pack(side='left')

root.mainloop()