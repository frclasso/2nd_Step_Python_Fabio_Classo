#!/usr/bin/env python3

from tkinter import *
root = Tk()

# criando uma caixa de texto
text = Text(root, width=40, height=10)
text.pack()

# inserindo texto
text.insert('1.0', 'As praias desertas continuam esperando por nos dois.\n\n\n\n\n\nO Vento '
                   'que venta lá fora...'
                   '\no barco que nao vai voltar.')

# separação de palavras
text.config(wrap='word')

# obtendo o texto
print(text.get('1.0', '1.end')) # do inicio da primeira linha até o final da primeira linha
# inserindo mais texto
text.insert('1.0 + 2 lines', 'Pablo Neruda')
text.insert('1.0 + 2 lines lineend', ' \nPoeta Chileno \nPremio Nobel de Literatua 1971.')

# deletando texto
text.delete('1.0')  # deleta o primeiro caractere 'A'
text.delete('1.0', '1.0 lineend') # deletou a primeira linha
text.delete('1.0', '3.0 lineend + 1 chars') # deleteou duas linhas em branco e a linha 'Pablo Neruda'

# subistituindo texto
text.replace('1.0', '1.0 lineend', "Pablo Neruda, nascido Ricardo Eliécer Neftalí Reyes Basoalto") # subistitui a primeira linha

# bloquenando alterações com sate = 'disabled'
text.config(state='disabled') # Nao permite sequer selecionar o texto
text.delete('1.0', 'end') # nao é possivel pois a edição de texto está desabilitada

text.config(state='normal')

root.mainloop()