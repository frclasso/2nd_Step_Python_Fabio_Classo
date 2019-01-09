#!/usr/bin/env python3

'''Creating additional top-level windows'''
from tkinter import *
root = Tk()

window = Toplevel(root) # root é a a janela pai/parent
window.title('New Window') # renomeamos a janela filha/child

window.lower()  # posiciona a janela filha sobre a janela pai
window.lift(root)

#window.state('zoomed')  # expande a janela filha
#window.state('iconic')  # minimiza a janela na barra de tarefas
#window.state('normal')  # desfaz zoomed e inonic
#print(window.state())  # imprime o estado atual da janela

#window.iconify() # minimiza a janela na barra de tarefas

#window.deiconify() # maximiza a janela


# Por padrao janelas são definidas com o tamanho 200x200
# caso queira alterar o padrao devemos utilizar o método geometry

window.geometry('640x480+50+100') # width, height, distancia esq da tela, distancia superior tela

window.resizable(False, False) # impossibilita modificar o tamanho via mouse

# criando valores máximo e mínimo para a janela
window.maxsize(640, 480)
window.minsize(200, 200)

window.resizable(True, True)

#root.destroy() destroi ambos os widgets

root.mainloop()