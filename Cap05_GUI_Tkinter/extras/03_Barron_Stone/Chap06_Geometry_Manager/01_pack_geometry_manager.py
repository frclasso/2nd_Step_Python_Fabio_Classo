#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
root = Tk()

# pack() sem nenhum parametro insere o label no centro e no alto
#ttk.Label(root, text="Hello, Tkinter", background="yellow").pack()

# pack(fill= X), preenche todo espaço disponivel no widget pai
#ttk.Label(root, text="Hello, Tkinter", background="yellow").pack(fill=X)  # X =  horizontal
# Y = vertical, BOOTH = ambas as direcoes

# Utilizamos a propriedade expand=True para expandir em ambas as direções
# ttk.Label(root, text="Hello, Tkinter", background="yellow").pack(fill=BOTH, expand=True)

# Adicionando multiplos widgets
# ttk.Label(root, text="Hello, Tkinter Yellow", background="yellow").pack(fill=BOTH, expand=True)
# ttk.Label(root, text="Hello, Tkinter Blue", background="blue").pack(fill=BOTH) # nao expande
# ttk.Label(root, text="Hello, Tkinter Green", background="green").pack(fill=BOTH, expand=True)

# Exibindo os widgets lado a lado
# ttk.Label(root, text="Hello, Tkinter Yellow! ", background="yellow").pack(side=LEFT)
# ttk.Label(root, text="Hello, Tkinter Blue! ", background="blue").pack(side=LEFT)
# ttk.Label(root, text="Hello, Tkinter Green! ", background="green").pack(side=LEFT)

# Ancorando o widget yellow na parte superior direita 'nw' north/west
# ttk.Label(root, text="Hello, Tkinter Yellow! ", background="yellow").pack(side=LEFT, anchor='nw')
# ttk.Label(root, text="Hello, Tkinter Blue! ", background="blue").pack(side=LEFT)
# ttk.Label(root, text="Hello, Tkinter Green! ", background="green").pack(side=LEFT)


# Inserindo padding externo padx, pady em widget blue
# ttk.Label(root, text="Hello, Tkinter Yellow! ", background="yellow").pack(side=LEFT, anchor='nw')
# ttk.Label(root, text="Hello, Tkinter Blue! ", background="blue").pack(side=LEFT, padx=10, pady=10)
# ttk.Label(root, text="Hello, Tkinter Green! ", background="green").pack(side=LEFT)

# Inserindo paddin interno no widget green, ipadx e ipady
ttk.Label(root, text="Hello, Tkinter Yellow! ", background="yellow").pack(side=LEFT, anchor='nw')
ttk.Label(root, text="Hello, Tkinter Blue! ", background="blue").pack(side=LEFT, padx=10, pady=10)
ttk.Label(root, text="Hello, Tkinter Green! ", background="green").pack(side=LEFT, ipadx=10,
                                                                        ipady=10)

# para inserirmos expand=True em todos os widget podemos usar um laço for
# juntamente com a propriedade root.pack_slaves()
for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH,expand=True)
    print(widget.pack_info())   # exibe o informações reativas ao package manager


root.mainloop()