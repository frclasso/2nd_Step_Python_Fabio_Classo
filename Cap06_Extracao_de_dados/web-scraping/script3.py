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


# for artist_name in artist_name_list_items:
#     print(artist_name.prettify())

# Usar .contents para pegar as tags <a> filhas
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    print(names)


"""Pegando o Conteudo de uma Tag

Para acessar apenas os nomes reais dos artistas, queremos focar no conteudo das tags <a> em vez de
imprimir toda a tag de link.

Podemos fazer isso com o .contents do Beautiful Soup, que ira retornar a tag filha com um tipo de 
dados lista do Python.

Vamos revisar o loop for para que, em vez de imprimir o link inteiro e sua tag, facamos a impressao
da lista das filhas (ou seja, os nomes completos dos artistas)."""


"""https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt"""