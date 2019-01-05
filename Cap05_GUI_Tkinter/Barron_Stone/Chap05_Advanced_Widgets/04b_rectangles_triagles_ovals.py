#!/ussr/bin/env python3

# rectangles, triangles, ovals

from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)

# criando um retangulo
rect = canvas.create_rectangle(160, 120, 480, 360) # retangulo necessita 4 parametros iniciais
# colorindo o retangulo
canvas.itemconfigure(rect, fill='green')

# criando um oval
oval = canvas.create_oval(160, 120, 480, 360) # cria um oval dentro do retangulo

# criando um arco
arc = canvas.create_arc(160,4,480,240)
# Podemos definir ou alterar onde nosso arco inicia e termina através da
                                            # propriedade canvas.itemconfigure
canvas.itemconfigure(arc, start=0, extent=180, fill='blue')

# criando um poligono qualquer
poly = canvas.create_polygon(160, 360,320, 480,480,360, fill='blue')

# Inserindo um texto
text = canvas.create_text(320, 240, text='Python', font=('Courier', 32, 'bold'))

# inserindo uma imagem usando método PhotoImage
logo = PhotoImage(file='python_logo.gif')
image = canvas.create_image(320,240, image=logo)

# movendo o texto para posição mais acima
canvas.lift(text)

# movendo a imagem para baixo
canvas.lower(image)
# a imagem foi jogada para a posição mais baixa de todas
# porem podemos posicionar a imagem logo abaixo do texto
canvas.lower(image, text)

# inserindo um botão ao canvas
button = Button(canvas, text='Click Me')
canvas.create_window(320, 60,window=button)
# podemos agrupar as propriedade dos objetos utilizando tags
canvas.itemconfigure(rect, tag='shape')
canvas.itemconfigure(oval, tag=('shape', 'round'))
canvas.itemconfigure('shape', fill='yellow') # alteramos as cores de preechimento do
# retangulo e do oval com a tag 'shape'

# caso precisemos saber quais tags um objetos possui
print(canvas.gettags(oval))

root.mainloop()