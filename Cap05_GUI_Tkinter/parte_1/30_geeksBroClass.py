#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.title("GeeksBro Class")


class GeeksBro:
    def __init__(self, root):
        self.text_btn = Button(root, text="ClickMe", command=self.say_hi)
        self.text_btn.pack()

        self.close_btn = Button(root, text="Close", command=root.quit)
        self.close_btn.pack()

    def say_hi(self):
        Label(root, text="Hi").pack()


geeks_bro = GeeksBro(root)
root.mainloop()
