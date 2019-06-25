#!/usr/bin/env python3

import csv

with open('bio_stats.csv', 'r') as csv_file:
    leitor = csv.reader(csv_file)
    #print(leitor) # end memoria
    cabecalho = next(leitor)
    print(cabecalho)
    # print(next(leitor))
    # print(next(leitor))
    # print(next(leitor))
    for line in leitor:
        print(line)