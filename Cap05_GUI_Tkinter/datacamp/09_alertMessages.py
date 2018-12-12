#!/usr/bin/env python3

import tkinter
import tkinter.messagebox


window = tkinter.Tk()
window.title("Alert message")

# creating a simple alert box
tkinter.messagebox.showinfo("Alert message", "This is just a alert message")

# creating a question to get the response from the user [Yes or No Question]
response = tkinter.messagebox.askquestion("Simple question", "Do you love Python?")

# If user clicks 'Yes' then it returns 1 else it returns 0
if response == 1:
    tkinter.Label(window, text="You love Python").pack()
else:
    tkinter.Label(window, text="You don't love Python").pack()

window.mainloop()