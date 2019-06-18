#!/usr/bin/env python3

import csv

with open('bio_stats.csv', 'r') as csv_file:
    leitor = csv.DictReader(csv_file)

    with open('bio_copy.csv', 'w') as new_file:
        fieldnames =['Name', 'Sex', 'Age', 'Weight(lbs)']

        escreve = csv.DictWriter(new_file, fieldnames=fieldnames,
                                 delimiter=',')
        escreve.writeheader()
        for line in leitor:
            del line['Height(in)']
            escreve.writerow(line)

print('feito...')