#!/usr/bin/env python3

import re

emails = """
FabioClasso@gmail.com
fabio.classo@floripacodegurus.edu
fabio-74-classo@my-work.net
"""

padrao = re.compile(r'[A-Za-z0-9\.\-]+@[A-Za-z\-]+\.(com|edu|net)')

matches = padrao.finditer(emails)
for match in matches:
    print(match)