from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()

def open_msg_box():
    messagebox.showwarning(
        "Event Triggered", "Button Clicked"
    )

root.geometry("400x400+300+300")
root.resizable(width=False, height=False)

frame = Frame(root)

theButton = ttk.Button(frame, text="Important Button", command=open_msg_box)

theButton['state'] = 'disable'
theButton['state'] = 'normal'
theButton.pack()

frame.pack()

style = ttk.Style()

# colors http://wiki.tcl.tk/37701 or use Hexadecimal colors
style.configure(
    "TButton",
    foreground="midnight blue",
    font='Times 20 bold italic',
    padding=20
)

print(ttk.Style().theme_names())
print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "foreground"))
print(style.lookup("TButton", "padding"))

# alterando o tema
ttk.Style().theme_use('aqua')

root.mainloop()