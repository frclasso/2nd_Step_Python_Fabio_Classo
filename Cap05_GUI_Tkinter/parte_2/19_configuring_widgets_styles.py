#!/usr/bin/env python3

# Configurando o estilo dos widgetes

# styles descreve como o widget vai ser exibido de acordo com com o estado em que se
# econtra
# active, disabled, focus, pressed, selected, background, readonly, alternate, invalid, hover

# Vamos trabalhar com temas, que são uma coleção de estilos para widgets
from tkinter import *
from tkinter import ttk
root = Tk()
button1 = ttk.Button(root, text='Botão 1')
button2 = ttk.Button(root, text='Botão 2')
button1.pack()
button2.pack()

# instanciando um objeto style
style = ttk.Style()

# varificando os estilos diposniveis no sistema
print(style.theme_names())  # ('aqua', 'clam', 'alt', 'default', 'classic')

# para verificar qual tema está em uso utilizamos style.theme_use()sem parametros
print(style.theme_use())

# para alterar o tema utilizamos styel.them_use() passando o nome do tema como parametro
style.theme_use('classic')
# retornando ao tema anterior
style.theme_use('aqua')


# Os nomes dos widgets por conveção usam a letra "T" antes do nome
# exemplo: TButton é o nome padrão para Button
# exceção Treeview, não TTreview

# para descobrir o nome padrão que o widget está utilizando usamos winfo_class()
print(button1.winfo_class())  # TButton

# para configurar o estilo do TButton para alterar a aparencia de todos os botões do programa
style.configure('TButton', foreground='blue')


# Podemos ainda criar estilos customizados derivados de outros estilos existentes
style.configure('Alarm.TButton', foreground='orange', font=('Arial', 24, 'bold'))
# aplicando o estilo customizado a button2
button2.config(style='Alarm.TButton')

# Podemos configurar o estilo baseado no estado no widget utilizando style.map()
style.map('Alarm.TButton', foreground=[('pressed', 'purple'), ('disabled', 'grey')])

button2.state(['disabled'])

# Para verificar todos os componentes intenos de estilo utilizamos o método layout()
print(style.layout('TButton')) # passando o nome do estilo como paramentro

# Para verificar as opções disponíveis para cada componente utilizamos
# styel.element_options('nome do componente')
print(style.element_options('Button_label'))

# para verificar qual configuração está em uso em um estilo específico
print(style.lookup('TButton', 'foreground')) # style, property

root = mainloop()