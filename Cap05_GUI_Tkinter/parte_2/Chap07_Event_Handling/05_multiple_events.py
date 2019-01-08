#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
root = Tk()

label1 = ttk.Label(root, text='Label 1')
label2 = ttk.Label(root, text='Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('Um botão qualuqer foi pressionado.'))
# <ButtonPress> corresponde a qualquer botão do mouse

# criando um evento para o botão 1 - left
label1.bind('<1>', lambda e:print('<1> Botão esquerdo pressionado em Label'))

# Se quisermos capturar esse mesmo evento em ambos os labels podemos faze-lo em root
# os eventos filhos(labels) herdarão do envento pai(root)
root.bind('<1>', lambda e: print('<1> Botão esq pressionado em root'))


# Agora ficamos com duas ações simultâneas em label1
# Podemos removê-la
label1.unbind('<1>')
label1.unbind('<ButtonPress>')

# Em caso de termos multiplas janelas em multiniveis em nosso programa pddemos usar o método
# root.bind_all
root.bind_all('<Escape>', lambda e:print('Tecla esc pressionada'))


root.mainloop()