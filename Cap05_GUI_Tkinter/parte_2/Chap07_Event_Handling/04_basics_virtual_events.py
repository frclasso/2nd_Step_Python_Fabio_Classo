#!/usr/bin/env python3


from tkinter import *
from tkinter import ttk
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy')) # Ctrl-c / Command-c
entry.bind('<<Paste>>', lambda e: print('Paste')) # Ctrl-v / Command-v

# adicionando um novo evento
entry.event_add('<<OddNumber>>','1', '3', '5', '7','9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number'))

# caso necessitemos informar quais keys disparam o envento, podemos exibí-las atrasvés da
# função event_info
print(entry.event_info('<<OddNumber>>'))

# podemos simular eventos
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

# Podemos deletar os eventos
entry.event_delete('<<OddNumber>>')
root.mainloop()