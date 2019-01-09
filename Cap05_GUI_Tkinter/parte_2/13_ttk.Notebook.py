#!/usr/bin/env python3

# notebook widget é usado para criar abas

from tkinter import *
from tkinter import ttk
root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

# criando frames para notebook
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

#adicionando ao notebook
notebook.add(frame1, text='One')
notebook.add(frame2, text='Two')

# inserindo um botão no frame
button = ttk.Button(frame1, text='ClickMe').pack()

# inserindo um novo frame com a função insert
frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text='Tree')

# excluindo frame3 com a função forget()
notebook.forget(1)  # o frame nao será destruído, continuará disponível em background

# adicionando novamente frame3
notebook.add(frame3, text='Tree')

#notebook.select() # retorna o ID da aba em uso

# modificando os estados das abas
notebook.tab(1, state='disabled')  # desabilita
notebook.tab(1, state='hidden')  # esconde a aba
notebook.tab(1, state='normal') # retorna ao estado inicial

print(notebook.tab(1, 'text')) # imprime o valor de texto da aba 1

print(notebook.tab(1)) # se não passarmos nenhum parâmetro retorna todos os valores possíveis
                        # para a aba selecionada

root.mainloop()