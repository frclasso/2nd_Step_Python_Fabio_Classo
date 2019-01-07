#!/usr/bin/env python3

# criando messageboxes, dialogs  e pop-ups
# nao utilizar from tkinter import *, importe apenas o modulo messagebox
from tkinter import messagebox

# showinfo message
# com dois parametros, title e message
#messagebox.showinfo(title='a friendly message', message='Hello Python')


# mesmo messagebox não sendo um tk widget o modulo tk ainda sim cria uma janela root em bakcground

# tres tipos de messagebox - showinfo(),showwarning() e showerror()

# criando uma janela yes/no
#messagebox.askyesno(title='Hungry', message='Do you want SAPM?')

# Messagebox types questions
# askyesno(), askokcancel(), asktrycancel(), askyesnocance(), askquestion()


# criando uma filedialog
# from tkinter import filedialog
# filename = filedialog.askopenfile()
# print(filename.name)

# filedialog
# sakdirectory(), asksavefile(mode), asksaveasfilename()
# askopenfile(mode), askopenfiles(mode), askopenfilename(),askopenfilenames()

# Obs,nenhum desses métodos abrem ou salvam nada, apenas retornam informações de
# arquivos ou diretorios



