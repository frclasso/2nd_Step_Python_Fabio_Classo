

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)
html_doc = r.text

soup = BeautifulSoup(html_doc)
# pretty_soup =(soup.prettify())
#
# print(pretty_soup)

# titulo
print(soup.title)

# links
a_tags = soup.find_all('a')
for links in a_tags:
    print(links.get('href'))