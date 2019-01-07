#!/usr/bin/env python3

from tkinter import *
root = Tk()


def shortcut(event):
    print(event)


# root.bind('<Control-c>', shortcut('Copy'))  # Nao acontece nada, erro, usar lambda
# root.bind('<Control-v>', shortcut('Paste'))

# root.bind('<Control-c>', lambda: shortcut('Copy')) # lambda aponta para a função shortcut
# root.bind('<Control-v>', lambda: shortcut('Paste'))
# TypeError: <lambda>() takes 0 positional arguments but 1 was given

# Esse erro ocorre porque o manipulador de eventos tenta passar objetos de informação de eventos
# como argumetos para a função lambda
# a função lambda não está esperando nenhum argumento

# Para corrigirmos isso
# adicionamos um argumento a função lambda para captura o objeto de eventos que está sendo passado
root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))



root.mainloop()