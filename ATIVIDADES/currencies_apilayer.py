#!/usr/bin/env python3

# -*-coding:utf-8 -*-

# https://currencylayer.com/


import json
from urllib.request import urlopen

with urlopen("http://www.apilayer.net/api"
             "/live?access_key=19b97a033fd712c7aca6d6060f44fbbe&format=1") as response:
    source = response.read()


data = json.loads(source)
#print(data)
print(type(data))

#print(json.dumps(data, indent=2))
#
usd_rates = dict()
for moedas, valores in data['quotes'].items():
    usd_rates[moedas] = valores  # passando moedas como keys do dicionario e valores como values

#print(usd_rates)
# print()
#
print(f"Convertendo 1 Dólar (USD) para Reais(BRL) => {usd_rates['USDBRL']}")
print(f"Convertendo 1 Dólar (USD) para EURO(EUR) => {usd_rates['USDEUR']}")
print(f"Convertendo 1 Dólar (USD) para Pesos Argentinos(ARS) => {usd_rates['USDARS']}")
print(f"Convertendo 1 Dólar (USD) para Dolar Australiano (AUD) => {usd_rates['USDAUD']}")
print(f"Convertendo 1 Dólar (USD) para Dolar Canadense (CAD) => {usd_rates['USDCAD']}")
print(f"Convertendo 1 Dólar (USD) para Peso Chileno (CLP) => {usd_rates['USDCLP']}")
print(f"Convertendo 1 Dólar (USD) para Peso Cubano (CUP) => {usd_rates['USDCUP']}")
