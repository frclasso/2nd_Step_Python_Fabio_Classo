#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()
window.title("GeeksBro Class")


class GeeksBro:
    def __init__(self, window):
        self.text_btn = tkinter.Button(window, text="ClickMe", command=self.say_hi)
        self.text_btn.pack()

        self.close_btn = tkinter.Button(window, text="Close", command=window.quit)
        self.close_btn.pack()

    def say_hi(self):
        tkinter.Label(window, text="Hi").pack()


geeks_bro = GeeksBro(window)
window.mainloop()
