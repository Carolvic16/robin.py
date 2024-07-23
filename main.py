# main.py

from processos import Processos
from escalonador import escalonador
from ler import ler
import time

# Criando uma instância da classe Processos
processos_obj = Processos()

# Definindo os tempos de execução para cada processo
tempos_processos = {
    "A": 5,
    "B": 7,
    "C": 9,
    "D": 10
}

# Chamando os métodos para iniciar os processos com os tempos específicos
processos_obj.A(tempos_processos["A"])
processos_obj.B(tempos_processos["B"])
processos_obj.C(tempos_processos["C"])
processos_obj.D(tempos_processos["D"])

# Esperando um tempo suficiente para os processos serem adicionados à fila
time.sleep(1)

# Obtendo a fila de processos atual como uma lista
fila_de_processos = processos_obj.get_fila_de_processos()

# Executando o escalonador com a fila de processos
escalonador(fila_de_processos, 5)