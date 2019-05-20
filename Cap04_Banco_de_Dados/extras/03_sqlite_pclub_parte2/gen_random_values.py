#!/usr/bin/env python3
# -*-coding:utf-8 -*-

"""Criando valores randômicos
Antes de mexer no banco de fato vamos criar uns valores
randômicos para popular o banco futuramente.

O arquivo gen_random_values.py gera idade, cpf, telefone, data e
cidade aleatoriamente. Para isso vamos importar algumas bibliotecas."""

import random
import rstr
import datetime


def gen_age():
    """gera um número inteiro entre 15 e 99"""
    return random.randint(15,99)


def gen_cpf():
    """"gera uma string com 11 caracteres numéricos. No caso, o primeiro parâmetro
    são os caracteres que serão sorteados e o segundo é o tamanho da string"""
    return rstr.rstr('1234567890', 11)


def gen_phone():
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4)
    )


def gen_timestamp():
    """A função gen_timestamp() gera um datetime no formato yyyy-mm-dd hh:mm:ss.000000.
    Repare no uso do random.randint(a,b) com um intervalo definido para cada parâmetro."""
    year = random.randint(1980, 2015)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    date = datetime.datetime(
        year, month, day, hour, minute, second, microsecond).isoformat(" ")
    return date


def gen_city():
    """A função gen_city() escolhe uma cidade numa lista com o comando random.choice(seq)"""
    list_city = [
        [u'São Paulo', 'SP'],
        [u'Belém', 'PA'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Goiânia', 'GO'],
        [u'Salvador', 'BA'],
        [u'Guarulhos', 'SP'],
        [u'Brasília', 'DF'],
        [u'Campinas', 'SP'],
        [u'Fortaleza', 'CE'],
        [u'São Luís', 'MA'],
        [u'Belo Horizonte', 'MG'],
        [u'São Gonçalo', 'RJ'],
        [u'Manaus', 'AM'],
        [u'Maceió', 'AL'],
        [u'Curitiba', 'PR'],
        [u'Duque de Caxias', 'RJ'],
        [u'Recife', 'PE'],
        [u'Natal', 'RN'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return random.choice(list_city)

gen_timestamp()