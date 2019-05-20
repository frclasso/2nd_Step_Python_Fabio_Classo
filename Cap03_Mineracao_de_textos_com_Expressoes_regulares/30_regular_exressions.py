#!/usr/bin/env python3

# re
# r => raw string


import re

text_to_search="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha  HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

codecla.com.br

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
"""

emails = """
FabioClasso@gmail.com
fabio.classo@codecla.edu
fabio-74-classo@my-work.net
"""

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://codecla.com.br
"""

sentence = 'Start a sentence and then bring it to an end'

# 1)
# print('\tTab')
# print(r'\tTab')


# 2
#pattern = re.compile(r'abc')
#pattern = re.compile(r'cba')
# matches = pattern.finditer(emails)
#
# for match in matches:
#     print(match)



#<re.Match object; span=(1, 4), match='abc'>
# span é o indice de inicio e fim do match
#print(text_to_search[67:69])

# 3)
# o caracter . (ponto) corresponde a qualquer caracter exceto nova linha \n
#pattern = re.compile(r'.') # precisa de \
#pattern = re.compile(r'codecla\.com\.br')
#matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)



# 4)
# digits
#pattern = re.compile(r'\d')


# 5)
# \D not a digit
#pattern = re.compile(r'\D')

# 6)
# \w word caracter (a-z, A-Z, 0-9, _)
#pattern = re.compile(r'\w')

# 7)
# \W Not word caracter
#pattern = re.compile(r'\W')

# 8)
# \s whitespaces (space, tab, newline)
#pattern = re.compile(r'\s')

# 9)
# \S Not whitespaces (space, tab, newline)
#pattern = re.compile(r'\S')

# 10)
# \b boundary 'Ha Ha'Ha
# pattern = re.compile(r'\bHa')

# 11)
#  \B boundary Ha Ha"Ha"
# pattern = re.compile(r'\BHa')
#
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)



# 12)
# ^ = Start , $ = end

# pattern = re.compile(r'end$')  # Usar Start, bring, end
#
# matches = pattern.finditer(sentence)

# 13 ) Phone number  => 321-555-4321 e 123.555.1234
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#
# matches = pattern.finditer(text_to_search)


# for match in matches:
#     print(match)

# 14)
# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

# 15)  # adcionar numero telefone com asteriscos

#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# pegando os numeros com 800 - 900
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# comenta esse e descomente o abaixo
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# comente o abaixo
# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

# 16 ) ranges
#pattern = re.compile(r'[a-zA-z]') # [a-zA-z]

# 17 ) negando com ^
#pattern = re.compile(r'[^a-zA-z]') # Not letters

# procurar cat e não bat

#pattern = re.compile((r'[^b]at'))

# 18) quantificadores

"""
    * 0 ou mais de um
    + 1 ou mais de um
    ? 0 ou 1
    {3} Numero exato
    {3,4} range

"""

#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)


# 19 ) Mr. e Mr

#pattern=re.compile(r'Mr\.')
#pattern=re.compile(r'Mr\.?') # ? o ponto passar ser opcional
#pattern=re.compile(r'Mr\.?\s[A-Z]')
# pattern=re.compile(r'Mr\.?\s[A-Z]\w+')  # exlui Mr. T, trocar para \w*
# pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # criando um grupo ou (Mr|Ms|Mrs)
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)


# 20 ) email

#pattern = re.compile(r'[a-zA-z]+@[a-zA-Z]+\.com')  # primeiro email
# pattern = re.compile(r'[a-zA-z.]+@[a-zA-Z]+\.(com|edu)') # segundo email
# pattern = re.compile(r'[a-zA-z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') # terceiro email
#
# matches = pattern.finditer(emails)
#
# for match in matches:
#     print(match)


# 21 ) urls

#pattern  = re.compile(r'https?://(www\.)?\w+')
#pattern = re.compile(r'https?://(www\.)?\w+\.\w+') # .com
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+\.?(br)?') # .com.br

# 22.A
# separando em grupos
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)(\.\w+)?')
#
# matches = pattern.finditer(urls)

# for match in matches:
#     #print(match)
#     print(match.group(4)) # 21.A

# 23 - sub urls

# sub_urls = pattern.sub(r'\2\3\4', urls)
# print(sub_urls)


# 24 findall
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#
# matches = pattern.findall(text_to_search)
#
# for match in matches:
#     print(match)


# 25 search

# pattern = re.compile(r'sentence')  # procurando a palavra 'sentence'
# matches = pattern.search(sentence)  # string sentence como parametro
# print(matches)

# 26 flag re.IGNORECASE

pattern = re.compile(r'start', re.IGNORECASE)  # procurando a palavra 'Start ou start'
matches = pattern.search(sentence)
print(matches)