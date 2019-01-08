#!/usr/bin/ env python3

from tkinter import *
from tkinter import ttk


class FeedBack:

    def __init__(self, master):

        self.header_frame = ttk.Frame(master) # nao se usa pack() diretamente no construtor

        self.header_frame.pack()  # exibindo na tela com pack, sem passar nenhum parâmetro
        # insere header_frame no nível mais acima da janela

        self.logo = PhotoImage(file='tour_logo.gif')
        ttk.Label(self.header_frame, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.header_frame, text='Thanks for Exploring!').grid(row=0, column=1)
        ttk.Label(self.header_frame, wraplength=300,
                  text=("We're glad you chose Explore California "
                        "for you recente adventure."
                        "Please tell us what you tought about "
                        "the 'Desert to sea' tour.")).grid(row=1, column=1)

        self.frame_content = ttk.Frame(master)
        # nao se usa pack() diretamente no construtor

        self.frame_content.pack() # exibindo com pack

        # ttk.Label(self.frame_content, text="Name:").grid(row=0, column=0)
        # ttk.Label(self.frame_content, text="Email:").grid(row=0, column=1)
        # ttk.Label(self.frame_content, text="Comments:").grid(row=2, column=0)
        #
        # self.entry_name = ttk.Entry(self.frame_content, width=24)
        # self.entry_email = ttk.Entry(self.frame_content, width=24)
        # self.text_comments = Text(self.frame_content, width=50, height=10)
        # # nao inserir o grid no construtor, fazer separado
        # self.entry_name.grid(row=1, column=0)
        # self.entry_email.grid(row=1, column=1)
        # self.text_comments.grid(row=3, column=0, columnspan=2)
        #
        # ttk.Button(self.frame_content, text='Submit').grid(row=4, column=0)
        # ttk.Button(self.frame_content, text='Clear').grid(row=4, column=1)

        '''DESCOMENTE O CODIGO ABAIXO E COMENTE O CODIGO ACIMA'''

        # inserindo padding externo
        # ttk.Label(self.frame_content, text="Name:").grid(row=0, column=0, padx=5)
        # ttk.Label(self.frame_content, text="Email:").grid(row=0, column=1, padx=5)
        # ttk.Label(self.frame_content, text="Comments:").grid(row=2, column=0, padx=5)
        #
        # self.entry_name = ttk.Entry(self.frame_content, width=24)
        # self.entry_email = ttk.Entry(self.frame_content, width=24)
        # self.text_comments = Text(self.frame_content, width=50, height=10)
        # # nao inserir o grid no construtor, fazer separado
        # self.entry_name.grid(row=1, column=0, padx=5)
        # self.entry_email.grid(row=1, column=1, padx=5)
        # self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)
        #
        # ttk.Button(self.frame_content, text='Submit').grid(row=4, column=0, padx=5)
        # ttk.Button(self.frame_content, text='Clear').grid(row=4, column=1, padx=5)

        '''DESCOMENTE O CODIGO ABAIXO E COMENTE O CODIGO ACIMA'''

        # alinhado widget com a propriedade sticky

        ttk.Label(self.frame_content, text="Name:").grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text="Email:").grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text="Comments:").grid(row=2, column=0, padx=5, sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width=24)
        self.entry_email = ttk.Entry(self.frame_content, width=24)
        self.text_comments = Text(self.frame_content, width=50, height=10)
        # nao inserir o grid no construtor, fazer separado
        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text='Submit').grid(row=4, column=0, padx=5,sticky='e', pady=5)
        ttk.Button(self.frame_content, text='Clear').grid(row=4, column=1, padx=5, sticky='w', pady=5)



def main():
    root = Tk()
    feedback = FeedBack(root)
    root.mainloop()


if __name__=="__main__":main()