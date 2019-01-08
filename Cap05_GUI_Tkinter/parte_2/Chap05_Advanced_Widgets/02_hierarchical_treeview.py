#!/usr/bin/env python3


# hierarchical treeview

from tkinter import *
from tkinter import ttk
root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()

# inserindo nodes
treeview.insert('', 0, 'item1', text='First item') # parent( '', se refere a root),
                                                    # index, iid=None(name), **kw(optional)

treeview.insert('', 1, 'item2', text='Second item')
treeview.insert('', 'end', 'item3', text='Third item')

# inserindo imagens
# primeiro vamos importar a imagem usando o construtor PhotoImage
logo = PhotoImage(file='python_logo.gif').subsample(10,10) # redimensionamos a logo para nao
                                                            # ficar muito grande

treeview.insert('item2', 'end', 'python', text='Python', image=logo)
# parent( parent(item2),index, iid=None(name), **kw(optional)

# podemos limitar o número de exibições alterando a configuração de height
treeview.config(height=5) # exibe apenas 5 items por vez

# movendo nodes dentro da árvore
treeview.move('item2', 'item1', 'end')  # item, parent, index

# Por padrão a árvore é exibida fechada, no entanto podemos modifiar para aberta
# utilizando a função open=True
treeview.item('item1', open=True)
treeview.item('item2', open=True)

print(treeview.item('item1', 'open')) # retorna 1 se estiver aberta/open

# removendo um node da árvore usando a função detach
treeview.detach('item3')  # isso não deleta o node

# movendo o item que havia sido desconectado
treeview.move('item3', 'item2', '0') # item, parent, index

# deletando completamente um node
treeview.delete('item3')

# Adicionando outra coluna, para exibição de detalhes ou informações do nosso programa
treeview.config(columns=('version'))\
# modificando a coluna criada
treeview.column('version', width=50, anchor='center') # name, option, **kw


# modificando a largura da janela da árvore principal
treeview.column('#0', width=150)

# Podemos ainda confirgurar o título exibindo nas janelas das árvores hierárquicas
# através da função heading
treeview.heading('version', text='Version') # name, valor

# definindo valores para items na coluna version
treeview.set('python', 'version', '3.4.1') # item, column, value

# agrupando propriedades atrvés de tags
treeview.item('python', tags='software')
treeview.tag_configure('software', background='yellow')

root.mainloop()