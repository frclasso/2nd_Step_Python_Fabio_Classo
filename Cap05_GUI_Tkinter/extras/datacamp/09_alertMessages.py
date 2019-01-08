#!/usr/bin/env python3

import tkinter
import tkinter.messagebox


window = tkinter.Tk()
window.title("Alert message")

# creating a simple alert box
tkinter.messagebox.showinfo(title="Alert message", message="This is just a alert message")

# creating a question to get the response from the user [Yes or No Question]
response = tkinter.messagebox.askquestion(title="Simple question", message="Do you love Python?")

# If user clicks 'Yes' then it returns 1 else it returns 0
if response == 'yes':
    tkinter.Label(window, text="You love Python").pack()
else:
    tkinter.Label(window, text="You don't love Python").pack()

window.mainloop()