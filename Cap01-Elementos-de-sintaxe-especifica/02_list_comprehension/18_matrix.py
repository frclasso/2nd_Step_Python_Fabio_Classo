#!/usr/bin/env python3

list_of_list = [ [1,2,3],[4,5,6],[7,8,9]]

# Vamos alinhar a lista em único nível
listaUnica = [y for x in list_of_list for y in x]
print(listaUnica)