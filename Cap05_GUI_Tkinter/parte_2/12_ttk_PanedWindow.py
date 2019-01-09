#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
root = Tk()

panedwindow = ttk.PanedWindow(root, orient=HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)

# criando frames
frame1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)

# adicionando frames no final com add
panedwindow.add(frame1, weight=1)
panedwindow.add(frame2, weight=4)  # frame2 é exibido com 4x a largura de frame1


frame3 = ttk.Frame(panedwindow, width=50, height=400, relief=SUNKEN)
# adicionando frames com posição definida através do método insert
panedwindow.insert(1, frame3)
# frame3 tem tamanho invariavel em relação aos demais frames

# excluindo um frame
#panedwindow.forget(1) # posição referente a frame3


root.mainloop()