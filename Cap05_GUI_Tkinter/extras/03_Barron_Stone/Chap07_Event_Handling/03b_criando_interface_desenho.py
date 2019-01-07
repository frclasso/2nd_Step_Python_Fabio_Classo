#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
root = Tk()

canvas = Canvas(root, width=640, height=480, background='Yellow')
canvas.pack()


def mouse_press(event):
    global prev # ao criar a interface draw
    prev = event # ao criar a interface draw


# Usamos bind para capturar os cliques do mouse
canvas.bind('<ButtonPress>', mouse_press)


def draw(event):
    # precisamos saber a localização previa do mouse e a atual, definimos uma varial global para isso
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y,  width=5)
    prev = event


def apaga(event):
    # precisamos saber a localização previa do mouse e a atual, definimos uma varial global para isso
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=5,  fill='Yellow') #mesma cor do canvas
    prev = event


canvas.bind('<B1-Motion>', draw)
canvas.bind('<B2-Motion>', apaga)

root.mainloop()