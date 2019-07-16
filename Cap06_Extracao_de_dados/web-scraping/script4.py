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
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    print(names)
    print(links)


"""Mas, e se quisermos tambem capturar as URLs associadas a esses artistas? Podemos 
extrair URLs encontradas dentro de tags <a> utilizando o metodo get('href') do Beautiful Soup.

A partir da saida dos links acima, sabemos que a URL inteira nao esta sendo capturada, entao 
vamos concatenar a string do link com o inicio da string da URL (nesse caso https://web.archive.org/)."""


"""https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt"""