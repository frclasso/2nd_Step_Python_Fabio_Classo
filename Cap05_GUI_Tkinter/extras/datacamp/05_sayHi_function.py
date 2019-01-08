#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.title('Say Hi')


def say_hi():
    Label(root, text="Hi!").pack()


Button(root, text="Click Me", command=say_hi).pack()
# command é usado quando ao clicar no botão chamar a função say_hi

root.mainloop()
