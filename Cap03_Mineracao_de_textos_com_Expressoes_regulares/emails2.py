#!/usr/bin/env python3

import re


padrao = re.compile(r'[A-Za-z0-9\.\-]+@[A-Za-z\-]+\.(com)(\.br)?')
with open('data.txt', 'r') as file:
    conteudo = file.read()
    matches = padrao.finditer(conteudo)
    for match in matches:
        print(match)