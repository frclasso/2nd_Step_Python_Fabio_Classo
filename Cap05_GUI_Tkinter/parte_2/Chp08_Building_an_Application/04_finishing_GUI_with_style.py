#!/usr/bin/ env python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class FeedBack:

    def __init__(self, master):

        # Vamos alterar o layout e o estilo dos widgets
        master.title('Explor California Feedback')
        master.resizable(False, False) # impede redimensionamento
        master.configure(background='#e1d8b9')

        # inserindo um estilo para os labels
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        self.header_frame = ttk.Frame(master)

        self.header_frame.pack()

        self.logo = PhotoImage(file='tour_logo.gif')
        ttk.Label(self.header_frame, image=self.logo).grid(row=0,column=0, rowspan=2)

        # Passando ao widget o estilo style='Header.TLabel
        ttk.Label(self.header_frame, text='Thanks for Exploring!',
                  style='Header.TLabel').grid(row=0, column=1)

        ttk.Label(self.header_frame, wraplength=300,
                  text=("We're glad you chose Explore California "
                        "for you recente adventure."
                        "Please tell us what you tought about "
                        "the 'Desert to sea' tour.")).grid(row=1, column=1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text="Name:").grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text="Email:").grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text="Comments:").grid(row=2, column=0, padx=5, sticky='sw')

        # alterando as fontes dos widgets
        self.entry_name = ttk.Entry(self.frame_content, width=24, font=('Arial', 10,))
        self.entry_email = ttk.Entry(self.frame_content, width=24, font=('Arial', 10,))
        self.text_comments = Text(self.frame_content, width=50, height=10, font=('Arial', 10))

        # nao inserir o grid no construtor, fazer separado
        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        # conectando as funções aos botões
        ttk.Button(self.frame_content, text='Submit', command=self.submit).grid(row=4,
                                                    column=0, padx=5,sticky='e', pady=5)

        ttk.Button(self.frame_content, text='Clear', command=self.clear).grid(row=4,
                                                    column=1, padx=5, sticky='w', pady=5)

        '''Vamos definir duas funções para criar ações para os botões 'Submit' e 'Clear' 
                                                            e ainda uma caixa pop-up'''
    def submit(self):
        print('Name:{}'.format(self.entry_name.get()))
        print('Email:{}'.format(self.entry_email.get()))
        print('Comments:{}'.format(self.text_comments.get(1.0, 'end'))) # parametros requeridos
        self.clear()
        # Aqui vamos criar uma janela pop-up para avisar ao usuario que deu tudo certo
        # inserir ao cabeçalho: from tkinter import messagebox
        messagebox.showinfo(title='Explore California Feedback', message='Comments Submitted!')

    def clear(self):
        self.entry_name.delete(0, 'end') # do inicio ao fim
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end') # da primeira linha ao fim


def main():
    root = Tk()
    feedback = FeedBack(root)
    root.mainloop()


if __name__=="__main__":main()