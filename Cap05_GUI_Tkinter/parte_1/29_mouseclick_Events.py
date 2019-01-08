#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.title("Mouse click events")

# definindo 3 diferente funções para eventos


def left_click(event):
    Label(root, text="Left Click").pack()


def middle_click(event):
    Label(root, text="Middle click").pack()


def right_click(event):
    Label(root, text="Right click").pack()


root.bind("<Button-1>", left_click)
root.bind("<Button-2>", middle_click)
root.bind("<Button-3>", right_click)


root.mainloop()