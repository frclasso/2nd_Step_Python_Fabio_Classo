#!/usr/bin/env python3
# -*-coding:utf-8 -*-

with open('alergylog.xlt') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ", sum(per_hour))