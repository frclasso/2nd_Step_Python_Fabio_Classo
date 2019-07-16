import re


urls = """
    https://www.google.com
    http://floripacodegurus.com.br
    https://youtube.com
    https://www.nasa.gov
"""

# pattern = re.compile(r'https?')  # o caractere "s" passar ser opcional

# pattern = re.compile(r'https?://(www\.)?') # www. passar ser opcional

# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # agrupando

padrao = re.compile(r'https?://(www\.)?(\w+)(\.\w+)(\.br)?')

matches = padrao.finditer(urls)
for match in matches:
    print(match)


# 0 => dominio inteiro, 1 = > www, 2=> nome dominio #3, top level domain

### comente o código acima - desconmente abaixo
#pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

#sub_urls = pattern.sub(r'\2\3', urls)

#print(sub_urls)