#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk
root = Tk()



# criando o canvas
canvas = Canvas(root, width=640, height=480, background='Green')
canvas.pack()

# definimos uma função para os diferentes eventos de mouse


def mouse_press(event):
    global prev # ao criar a interface draw
    prev = event # ao criar a interface draw
    print('type:{}'.format(event.type))
    print('widget:{}'.format(event.widget)) #exibe info do widget
    print('num:{}'.format(event.num)) # numero do botao do mouse que foi pressionado
    print('x:{}'.format(event.x))# coordenadas x em relação ao widget, não ao monitor de vídeo
    print('y:{}'.format(event.y))# coordenadas y
    # caso precisemos saber as coordenadas em relação a tela usamos x_root e y_root
    print('x_root:{}'.format(event.x_root))
    print('y_root:{}'.format(event.y_root))

# Usamos bind para capturar os cliques do mouse
canvas.bind('<ButtonPress>', mouse_press)


# criando uma interface par desenhar linhas
# def draw(event):
#     # precisamos saber a localização previa do mouse e a atual, definimos uma varial global para isso
#     global prev
#     canvas.create_line(prev.x, prev.y, event.x, event.y,  width=5)
#     prev = event
#
#
# canvas.bind('<B1-Motion>', draw)

root.mainloop()
