#!/usr/bin/env python3

#-*-coding:utf-8-*-

# web scraping com BeautifulSoup
import requests
from bs4 import BeautifulSoup

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# Remover links inferiores
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

artist_name_list = soup.find(class_='BodyText')

artist_name_list_items = artist_name_list.find_all('a')


for artist_name in artist_name_list_items:
    print(artist_name.prettify())




"""Removendo Dados Superfluos

Ate agora, conseguimos coletar todos os dados de texto do link dentro de uma secao <div> da
nossa pagina web. No entanto, nao queremos ter os links inferiores que nao fazem referencia
aos nomes dos artistas. Por isso, vamos trabalhar para remover essa parte.

Para remover os links inferiores da pagina, vamos clicar novamente com o botao direito e 
Inspecionar o DOM. Veremos que os links na parte inferior da secao <div class="BodyText"> 
estao contidos em uma tabela HTML: <table class="AlphaNav">:"""


"""Podemos, portanto, usar o Beautiful Soup para encontrar a classe AlphaNav e usar o 
metodo decompose() para remover uma tag da arvore de analise e depois destrui-la juntamente 
com seu conteudo.

Usaremos a variavel last_links para fazer referencia a esses links inferiores e adiciona-los ao 
arquivo do programa:"""

"""https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt"""