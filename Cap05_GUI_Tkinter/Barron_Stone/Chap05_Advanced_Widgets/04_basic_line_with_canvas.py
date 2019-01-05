#!/usr/bin/env python3

from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack() # instancia o objeto

#definindo o tamanho da janela
canvas.config(width=640, height=480)
# criando uma linha
line = canvas.create_line(160, 360, 480,120, fill='blue') # coordenadas
# alterando a propriedade cor
canvas.itemconfigure(line, fill='green')

# exibindo as coordenadas
print(canvas.coords(line))
# alterando as coordenadas
canvas.coords(line, 0,0, 320, 240, 640,0)

# alterando a forma da linha
canvas.itemconfigure(line, smooth=True)
#canvas.itemconfigure(line,splinesteps=5)
canvas.itemconfigure(line,splinesteps=15)

# deletando a linha
canvas.delete(line)







root.mainloop()