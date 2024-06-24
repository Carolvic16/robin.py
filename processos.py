# Processos.py

from collections import deque
import threading

# Define a função que simula um processo com um ID e uma fila.
def quantum(process_id, deque, tempo):
    deque.append((process_id, tempo))
    print(f'Processo {process_id} adicionado à fila com {tempo} segundos restantes ')
    
class Processos:
    def __init__(self):
        self.fila_de_processos = deque()

    def setP1(self, tempo):
        t1 = threading.Thread(target=quantum, args=(1, self.fila_de_processos, tempo))
        t1.start()
        print(f'Thread para P1 iniciada com tempo de {tempo} segundos')

    def setP2(self, tempo):
        t2 = threading.Thread(target=quantum, args=(2, self.fila_de_processos, tempo))
        t2.start()
        print(f'Thread para P2 iniciada com tempo de {tempo} segundos')

    def setP3(self, tempo):
        t3 = threading.Thread(target=quantum, args=(3, self.fila_de_processos, tempo))
        t3.start()
        print(f'Thread para P3 iniciada com tempo de {tempo} segundos')

    def setP4(self, tempo):
        t4 = threading.Thread(target=quantum, args=(4, self.fila_de_processos, tempo))
        t4.start()
        print(f'Thread para P4 iniciada com tempo de {tempo} segundos')

    def get_fila_de_processos(self):
        return list(self.fila_de_processos)  # Retorna a fila de processos como uma lista
