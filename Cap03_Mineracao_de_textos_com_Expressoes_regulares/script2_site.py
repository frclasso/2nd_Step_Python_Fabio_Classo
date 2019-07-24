#!/usr/bin/env python3

import re

frase = 'Floripa Code Gurus Escola de Tecnologia em Florianopolis'

padrao = re.compile(r'Florianopolis$')

matches = padrao.finditer(frase)
for match in matches:
    print(match)

