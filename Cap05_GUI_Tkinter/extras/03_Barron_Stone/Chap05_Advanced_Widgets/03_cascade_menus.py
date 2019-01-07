#!/usr/bin/env python3

# cascade menus não é parte do módulo ttk
from tkinter import *
root = Tk()
root.option_add('*tearOff', False)
# criando um menubar
menubar = Menu(root) # Menu é propriedade interna do modulo tkinter
root.config(menu=menubar)  # property, object
# criando items de menu,que são filhos de menubar
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar) # help é palavra chave por isso o uderscore depois
# adicionando os items criados ao menu
menubar.add_cascade(menu=file, label='File')
menubar.add_cascade(menu=edit, label='Edit')
menubar.add_cascade(menu=help_, label='Help')

# Adicionando funcionalidades aos items de menu
file.add_command(label='New', command=lambda: print('New File'))

# Podemos adicionar separadores ente os comandos
file.add_separator()

# Adicionando mais comandos
file.add_command(label='Open', command=lambda: print('Opening File...'))
file.add_command(label='Save', command=lambda: print('Save File'))

# Podemos associar atalhos aos comandos através  da função accelerator
file.entryconfig('New', accelerator='Ctrl + N')  # nome, atalho

# inserindo imagens
logo = PhotoImage(file='python_logo.gif').subsample(10,10) # subsample para redimenssionar
file.entryconfig('Open', image=logo, compound='left')

# caso seja necessario desabilitar uma função sem deletá-la
#file.entryconfig('Open', state='disabled')

# criando submenus
# vamos criar um submenu em file>save
# primeiro vamos remover o comando Save de 'file'
file.delete('Save')
# criando um novo objeto 'save' filho de 'file'
save = Menu(file)
#adicionando ao menu
file.add_cascade(menu=save, label='Save')
# add comandos
save.add_command(label='Save as', command=lambda: print('Saving As'))
save.add_command(label='Save all', command=lambda: print('Saving All'))

# Adicionando radio button ao menu 'Edit'
choice = IntVar()
edit.add_radiobutton(label='One', variable=choice, value=1)
edit.add_radiobutton(label='Two', variable=choice, value=2)
edit.add_radiobutton(label='Tree', variable=choice, value=3)



root.mainloop()