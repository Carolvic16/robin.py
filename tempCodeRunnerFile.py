# main.py
from collections import deque, defaultdict
import threading
from threading import Thread
import time
from time import sleep


from Processos import Processos

# Criando uma instância da classe Processos
processos = Processos()

# Chamando o método  para iniciar um processo
processos.setP1("P1", 5)
processos.setP2 ("P2", 7)
processos.setP3 ("P3",9)
processos.setP4 ("P4",10)

# Esperando um tempo para demonstração
time.sleep(5)

# Imprimindo a fila de processos atual
print("Fila de Processos:", processos.get_fila_de_processos())