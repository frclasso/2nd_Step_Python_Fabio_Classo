#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
root = Tk()

# Para que o nosso programa capture os eventos de teclado utilizaremos o método bind
# sobre a janela principal, root

def key_press(event):
    print('type:{}'.format(event.type)) # tipo
    print('widget:{}'.format(event.widget)) # o nome do widget que ocorreu o evento
    print('char:{}'.format(event.char)) # o carctere que disparou o evento
    print('keysym:{}'.format(event.keysym)) # simbolo da chave(key)
    print('keycode:{}'.format(event.keycode)) # contem o codigo numerico da chave(key) pressionada

root.bind('<KeyPress>', key_press)
# o primeiro parametro é uma string contendo especialmente descrições de
# parametros de eventos que pretendemos ouvir
# segundo parametro é nome de retorno do evento ou método que se pretende executar

root.mainloop()