#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text='Hello, Tkinter!')
label.pack()

 # Vamos alterar algumas propriedades

label.config(text='Howdy, Tkinter!')
label.config(text="Howdy Tkinter! It's been a while since  we last met. Great to see you again.")

label.config(wraplength=150) # empacota o texto em 150 pixels
label.config(justify=CENTER) # alinhamento centralizado

# foreground e background, alterando as cores
label.config(foreground='blue', background='black')  # nao alterou o background

# Alterando a fonte
label.config(font=('Courier', 18, 'bold'))  # Passamos uma tupla de argumentos para a font

# exibindo uma imagem ao invés de texto
# usaremos a biblioteca image - PhotoImage
logo = PhotoImage(file='python_logo.gif')
label.config(image=logo)


# Agora vamos exibir texto e imagem ao mesmo tempo
# Primeiro vamos reduzir nosso texto, voltando ao original
label.config(text='Howdy,Tkinter!')

# Vamos utilizar a propriedade compound para selecionar qual será exibido
label.config(compound='text')

# Exibindo ambos, o texto no meio da janela sobre a imagem
label.config(compound='center')

# colocando a imagem a esquerda do texto
label.config(compound='left')

root.mainloop()