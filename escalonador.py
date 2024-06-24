import time


def escalonador(processos, tempo_de_quantum):
    while processos:
        processo_atual, tempo_restante = processos.pop(0)
        if tempo_restante > tempo_de_quantum:
            print(f'Executando Processo {processo_atual} por {tempo_de_quantum} segundos')
            time.sleep(tempo_de_quantum)
            print(f'Processo {processo_atual} ainda tem {tempo_restante - tempo_de_quantum} segundos restantes')
            processos.append((processo_atual, tempo_restante - tempo_de_quantum))
        else:
            print(f'Executando Processo {processo_atual} por {tempo_restante} segundos')
            time.sleep(tempo_restante)
            print(f'Processo {processo_atual} finalizado')