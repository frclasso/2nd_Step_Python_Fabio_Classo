#!/usr/bin/env python3

'''Organizing widgets with frames'''


from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root)
frame.pack()  # usamos o gerenciador geometrico pack para criar um frame em root
frame.config(height=100, width=200)
frame.config(relief=RIDGE)
ttk.Button(frame, text='Click Me').grid() # usamos o gerenciado geometrico grid()
                                            # para criar um botao em frame
frame.config(padding=(30, 15))

# criando um LabelFrame
ttk.LabelFrame(root, height=100, width=200, text='My frame').pack()
# voltamos a utilizar pack() pois estamos criando um frame em root


root.mainloop()