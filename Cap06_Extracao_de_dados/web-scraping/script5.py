#!/usr/bin/env python3

#-*-coding:utf-8-*-

# web scraping com BeautifulSoup
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# Remover links inferiores
last_links = soup.find(class_='AlphaNav')
last_links.decompose()


# criar um arquivo para gravar
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name','Link'])

artist_name_list = soup.find(class_='BodyText')

artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    # print(names)
    # print(links)
    f.writerow([names, links])

"""Gravando os Dados em um Arquivo CSV"""


"""https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt"""