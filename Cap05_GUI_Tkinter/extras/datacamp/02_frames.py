#!/usr/bin/env python3


import tkinter

window =tkinter.Tk()

window.title('Frame')

# criando 2 frames um TOP e outro BOTTOM

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")

# criando widgets para os frames top e bottom

btn1 = tkinter.Button(top_frame, text="Button 1", fg="red").pack()
btn2 = tkinter.Button(top_frame, text="Button 2", fg="green").pack()
btn3 = tkinter.Button(bottom_frame, text="Button 3", fg="purple").pack(side='left')
btn4 = tkinter.Button(bottom_frame, text="Button 4", fg="blue").pack(side='left')

window.mainloop()