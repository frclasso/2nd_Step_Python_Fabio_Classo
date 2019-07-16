#!/usr/bin/env python3

import re

padrao = re.compile(r'[89]00[-]\d{3}.\d{4}')

with open("texto1.txt", 'r', encoding='utf-8') as file:
    conteudo = file.read()
    matches = padrao.finditer(conteudo)
    for match in matches:
        print(match)
