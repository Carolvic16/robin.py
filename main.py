from Processos import Processos
import time

# Função para executar e finalizar os processos em uma fila
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

# Lendo processos de um arquivo txt
def ler_processos_do_arquivo(nome_do_arquivo):
    processos = []
    with open(nome_do_arquivo, 'r') as file:
        for linha in file:
            processo_id, tempo = linha.strip().split(',')
            processos.append((processo_id, int(tempo)))
    return processos

# Nome do arquivo de processos
nome_do_arquivo = 'processos.txt'

# Lendo processos do arquivo
fila_de_processos = ler_processos_do_arquivo(nome_do_arquivo)

# Definindo o tempo de quantum (ajustar conforme necessário)
tempo_de_quantum = 5

# Executando o escalonador com a fila de processos
escalonador(fila_de_processos, tempo_de_quantum)
