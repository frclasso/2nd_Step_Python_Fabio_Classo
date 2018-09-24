#!/usr/bin/env python3


key = 'got'

print({'already':(lambda: 2 + 2),
 'got':(lambda: 2 * 4),
 'one':(lambda: 2 ** 6)}[key]())


def f1():return 2 + 2
def f2():return 2 * 4
def f3():return 2 ** 6





key = 'one'
print({'already':f1, 'got':f2, 'one':f3}[key]())