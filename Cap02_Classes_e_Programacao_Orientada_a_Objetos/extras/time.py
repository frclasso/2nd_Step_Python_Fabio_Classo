#!/usr/bin/env python3


class Horario:

    def exibeHora(time):
        print(str(time.horas) + ':' + str(time.minutos) + ':' + str(time.segundos))

    def incrementar(horario, segundos):
        horario.segundos = horario.segundos + segundos

        while horario.segundos >= 60:
            horario.segundos = horario.segundos - 60
            horario.minutos = horario.minutos + 1

        while horario.minutos >= 60:
            horario.minutos = horario.minutos - 60


horaCorrente = Horario()
horaCorrente.horas = 9
horaCorrente.minutos = 14
horaCorrente.segundos = 30
horaCorrente.exibeHora()

horaCorrente.incrementar(500)
horaCorrente.exibeHora()