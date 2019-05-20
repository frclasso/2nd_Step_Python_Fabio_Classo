#!/.usr/bin/env python3

from tkinter import *

root = Tk()

root.title('Cadastro de alunos')

lb1 = Label(root, text='Nome')
lb1.grid(row=0,column=0)

ed1 = Entry(root)
ed1.grid(row=0,column=1,sticky=W)

lb2 = Label(root, text='Sobrenome')
lb2.grid(row=1,column=0)

ed2 = Entry(root)
ed2.grid(row=1,column=1, sticky=W)

lb3 = Label(root, text='e-mail')
lb3.grid(row=2,column=0)

ed3 = Entry(root)
ed3.grid(row=2,column=1, sticky=W)

# 2

Label(root, text='Selcione o curso').grid(row=4, column=0, sticky=W)
Radiobutton(root, text='Python', value=1).grid(row=5, column=0, sticky=W)
Radiobutton(root, text='C#', value=2).grid(row=6, column=0, sticky=W)
Radiobutton(root, text='PHP', value=3).grid(row=7, column=0, sticky=W)
Radiobutton(root, text='Excel', value=4).grid(row=8, column=0, sticky=W)

#3

Label(root, text='Horario').grid(row=4, column=1, sticky=W)
Checkbutton(root, text='Manhã - 08 as 12h').grid(row=5, column=1, sticky=W)
Checkbutton(root, text='Tarde - 13 as 17h').grid(row=6, column=1, sticky=W)
Checkbutton(root, text='Noite - 19 as 23h').grid(row=7, column=1, sticky=W)

Label(root, text="Comentários").grid(row=9, column=0, sticky=W)
Entry(root, width=50).grid(row=9, column=1, sticky=W+E)
Button(root, text='Submit').grid(row=9,column=3,columnspan=3,sticky=W+E)

# Criando um frame para imagem

from PIL import Image
from PIL import ImageTk

frame = Frame(root)
frame.grid(row=0, column=3, rowspan=5, columnspan=3)

# Inserindo imagem

img = Image.open('logoCode_pequena.gif')
img = img.resize((100, 100), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
Label(frame, image=photoImg).grid(row=0, column=0)

root.mainloop()