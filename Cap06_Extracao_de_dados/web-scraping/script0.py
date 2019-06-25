#!/usr/bin/env pyton3

import requests

headers = {
    'User-Agent': 'Fabio Classo, Floripa Code Gurus',
    'From':'fabioclasso@floripacodegurus.com.br'
}

url = 'https://floripacodegurus.com.br'

page = requests.get(url, headers=headers)