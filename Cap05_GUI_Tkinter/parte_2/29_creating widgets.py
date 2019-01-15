#!/usr/bin/ env python3

from tkinter import *
from tkinter import ttk


class FeedBack:

    def __init__(self, master):

        # criando nosso frame header
        self.header_frame = ttk.Frame(master) # frame é filho da janela master

        # inserindo a logo
        self.logo = PhotoImage(file='tour_logo.gif')
        # criando os labels
        ttk.Label(self.header_frame, image=self.logo)
        ttk.Label(self.header_frame, text='Thanks for Exploring!')
        ttk.Label(self.header_frame, text="We're glad you chose Explore California for you"
                                          "recente adventure."
                                          "\nPlease tell us what you tought about the "
                                          "'Desert to sea' tour.")


        # criando nosso frame de conteúdo
        self.frame_content = ttk.Frame(master)

        ttk.Label(self.frame_content, text="Name:")
        ttk.Label(self.frame_content, text="Email:")
        ttk.Label(self.frame_content, text="Comments:")

        # entrada de dados do campos criados acima
        self.entry_name = ttk.Entry(self.frame_content, width=24)
        self.entry_email = ttk.Entry(self.frame_content, width=24)

        # Text nao pertence ao módulo ttk
        self.text_comments = Text(self.frame_content, width=50, height=10)

        # criando os botões
        ttk.Button(self.frame_content, text='Submit')
        ttk.Button(self.frame_content, text='Clear')


def main():
    root = Tk()
    feedback = FeedBack(root)
    root.mainloop()

if __name__=="__main__":main()