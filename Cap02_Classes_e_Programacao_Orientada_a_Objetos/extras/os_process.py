    #!/usr/bin/env python3
# -*-coding:utf-8 -*-
import os, sys, datetime


class MeuComputador:

    def users_process(self):
        "Verifica o usuario conectado e processos que estao rodando"

        print('Usuarios e processos****')
        print('Retorna id do usuario atual:{} '.format(os.getuid()))
        print('Retorna id do grupo atual: {}'.format(os.getgid()))
        print('Retorna id do  processo atual: {}'.format(os.getpid()))
        print('Retorna id do  processo Pai : {}'.format(os.getppid()))
        print()

    def sistemaOp(self):
        """Verifica informacoes do sistema operacional"""
        print('Sobre o computador e Sistema Operacional****')
        print('Qual seu sistema operacional? {}'.format(os.uname()[0]))
        print('Qual nome do computador? {}'.format(os.uname()[1]))
        print('Versao do Kernel:  {}'.format(os.uname()[2]))
        print('Versao:  {}'.format(os.uname()[3]))
        print('Arquitetura: {}'.format(os.uname()[4]))
        print('Diretorio atual: {}'.format(os.getcwd()))
        print('Verificando se diretorio extras existe: {}'.format(os.path.isdir('extras')))
        print()

    def verficaVersao(self):
        "Exibe a versao do Python instalada atraves do modulo sys"
        v = sys.version_info
        print('Python version {}.{}.{}'.format(*v))
        w = sys.platform
        print(w)
        z = os.name
        print(z)

    def listandoDiretorio(self):
        "Lista o conteudo do diretorio atual."
        return os.system('ls -la')

    def verificaHora(self):
        "Exibe data calendario completo, data e hora do sistema"
        now = datetime.datetime.now()
        print(now)
        print(now.year, now.month, now.day, now.hour, now.minute, now.second)
        print(f'Calendario: {now.year}/{now.month}/{now.day} e Hora: {now.hour}:{now.minute}:{now.second}')


processo = MeuComputador()
#processo.users_process()
#print(processo.users_process.__doc__)
#processo.sistemaOp()
#print(processo.sistemaOp.__doc__)
#processo.verficaVersao()
#processo.diretorio()
#print(processo.diretorio.__doc__)
#print(processo.verificaHora.__doc__)
# processo.verificaHora()
# processo.users_process()
# processo.listandoDiretorio()
#processo.verficaVersao()
processo.sistemaOp()