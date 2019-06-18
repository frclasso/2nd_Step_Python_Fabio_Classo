import time

# caculando o tempo de execução de uma determinada função


# definindo nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # calcula tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        #Formata a mensagem que será mostrada na tela
        print("[{funcao}] - Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper

# decorando a funcao
@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

main()
