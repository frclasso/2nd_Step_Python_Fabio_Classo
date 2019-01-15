#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
root = Tk()

"""Se necessitarmos alterar um label futuramente em nosso programa, precisamos
salvar esse label em uma variável.
Vamos ver o que acontece quando salvamos a saída do nosso método construtor
com o package manager pack() conectado"""

# primeiro criamos a variável label
# label = ttk.Label(root, text="Hello, Tkinter Yellow! ",
#                   background="yellow").pack(side=LEFT, anchor='nw')
# print(label)
# A saída  será None, não salvamos uma referência desse label

# Sequisermos salvar um referencia para uso posterior, precisamos
# primeiro salvar o label em uma variavel
label = ttk.Label(root, text="Hello, Tkinter Yellow! ",
                  background="yellow")
label.pack(side=LEFT, anchor='nw')# e em seguida chamar o método pack sobre a variável criada
print(label.winfo_id())


ttk.Label(root, text="Hello, Tkinter Blue! ", background="blue").pack(side=LEFT, padx=10, pady=10)
ttk.Label(root, text="Hello, Tkinter Green! ", background="green").pack(side=LEFT, ipadx=10,
                                                                        ipady=10)

# para inserirmos expand=True em todos os widget podemos usar um laço for
# juntamente com a propriedade root.pack_slaves()
for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH,expand=True)
    print(widget.pack_info())   # exibe o informações relativas ao package manager

label.pack_forget()

root.mainloop()