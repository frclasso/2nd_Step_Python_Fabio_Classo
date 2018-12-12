#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()
window.title("Simple shapes")

# creating canvas areas of width and height 500px

canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()

# create_line is used to create a line
# Paramters: starting x-point, start y-point, width, height, fill
line1 = canvas.create_line(25,25,250,150)
# parameter => fill = color_name
line2 = canvas.create_line(25,250,250,150, fill='red')

# create_rectangule is used to create rectangules.
# Parameters =>  starting x-point, start y-point, width, height, fill
# starting point the coordinates of top-left point of rectangle

rect = canvas.create_rectangle(500,25,175,75, fill='green')

# delete shapes using delete method passing the name of variable as parameter
#canvas.delete(line1)

# it's possible to delete all shapes using 'ALL' as  parameter to the 'delete' method
#canvas.delete(tkinter.ALL)
window.mainloop()