#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
root = Tk()

#
# def callback():
#     print('In the callback')
#
#
# ttk.Button(root, text='Click Me!', command=callback).pack()  # command = callback sem parenteses
# # passamos apenas o nome da função a ser executada


# Exemplo 2, vamos passar um valor como parâmetro para a função

# def callback(number):
#     print(number)
#
#
# ttk.Button(root, text='Click Me 1', command=callback(1)).pack()  # erro comum, passar valores
# # como parametro, RODE O PROGRAMA
# ttk.Button(root, text='Click Me 2', command=callback(2)).pack()
# ttk.Button(root, text='Click Me 3', command=callback(3)).pack()
# ao inves de passar o nome da função a ser executada para a propriedade command, executa a função
# e passar valor de callback para command, logo a função callback não retorna nada e
# command é definida como None, logo os notões não executam nenhuma ação ao serem executados

# corrigindo esse erro,
# utilizamos a função lambda para apontar para a função callback
def callback(number):
    print(number)


ttk.Button(root, text='Click Me 1', command=lambda:callback(1)).pack()
ttk.Button(root, text='Click Me 2', command=lambda:callback(2)).pack()
ttk.Button(root, text='Click Me 3', command=lambda:callback(3)).pack()



root.mainloop()