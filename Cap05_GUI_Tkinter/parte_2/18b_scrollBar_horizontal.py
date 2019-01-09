#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
root = Tk()

# definindo a área onde a scrollbar vai atuar
canvas=Canvas(root, scrollregion=(0,0, 640, 480), bg='green')

# utilizamos o modulo ttk para criar  a scrollbar
xscroll = ttk.Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
yscroll = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
canvas.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

canvas.grid(row=1, column=0)
xscroll.grid(row=2, column=0, sticky='ew')
yscroll.grid(row=1, column=1, sticky='ns')

# capturando os cliques do mouse


# def canvas_click(event):
#     x = event.x
#     y = event.y
#     canvas.create_oval((x-5, y-5, x+5, y+5), fill='green')


"""No entando quando rolamos a(s) barra(s) e fazemos novos cliques,
os mesmos não aparecem no local exato para onde movemos o canvas 
com o scrollbar. Isso ocorre porque o método bind não entende que
rolamos a barra."""

# para corrigir este problema altere a função canvas_click
# x = canvas.canvasx(event.x)
# y = canvas.canvasy(event.y)

# descomente o código abaixo:


def canvas_click(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_oval((x-5, y-5, x+5, y+5), fill='green')


canvas.bind('<1>', canvas_click)

root.mainloop()