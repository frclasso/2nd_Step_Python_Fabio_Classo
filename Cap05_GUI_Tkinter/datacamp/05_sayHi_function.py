#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()
window.title('Say Hi')


def say_hi():
    tkinter.Label(window, text="Hi").pack()


tkinter.Button(window, text="Click Me", command=say_hi).pack()
# command é usado quando ao clicar no botão chamar a função say_hi

window.mainloop()
