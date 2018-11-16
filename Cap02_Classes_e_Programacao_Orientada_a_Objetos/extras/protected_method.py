#!/usr/bin/env python3
# -*-coding:utf-8 -*-


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount)
# Erro: AttributeError: 'JustCounter' object has no attribute
#  '__secretCount'
