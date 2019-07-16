#!/usr/bin/env python3

#-*-coding:utf-8-*-

# web scraping com BeautifulSoup
import requests
from bs4 import BeautifulSoup
import csv



"""Recuperando Paginas Relacionadas

Criamos um programa que extraira dados da primeira pagina da lista de artistas cujos sobrenomes 
comecam com a letra Z. Porem, existem 4 paginas desses artistas no total, disponiveis no website.

Para coletar todas essas paginas, podemos executar mais iteracoes com loops for. Isso revisara 
a maior parte do codigo que escrevemos ate agora, mas empregara conceitos semelhantes.

Para comecar, vamos inicializar uma lista para manter as paginas:"""

f = csv.writer(open('z-artist-names_all.csv', 'w'))
f.writerow(['Name', 'Link'])

pages =[]
#Vamos preencher essa lista inicializada com o seguinte loop for:
for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Remover links inferiores
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        # print(names)
        # print(links)
        f.writerow([names, links])


"""https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt"""