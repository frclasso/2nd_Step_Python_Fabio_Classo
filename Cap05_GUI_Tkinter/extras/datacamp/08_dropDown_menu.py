#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()
window.title("Menu Drop Down")


def function():
    pass


# creta a root menu to insert all the sub menus
root_menu = tkinter.Menu(window)
window.config(menu=root_menu)

# creating sub menus in the root_menu
file_menu = tkinter.Menu(root_menu) # initializes a new sub menu in root_menu
root_menu.add_cascade(label="File", menu=file_menu)  # it creates the name of the sub menu
file_menu.add_command(label="New file...", command=function) # it adds a option to the sub menu 'command' parameter is used to do some action
file_menu.add_command(label = "Open files", command=function)
file_menu.add_separator() # it adds a line after the 'Open files' option
file_menu.add_command(label="Exit", command=window.quit)

# creating another sub menu

edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label ="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=function)
edit_menu.add_command(label="Redo", command=function)

window.mainloop()