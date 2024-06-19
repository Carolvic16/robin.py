import threading 
import time 

#DEFINICOES

TEMPO_DAS_INSTRUÇÕES { # estabelecido pelo exercício
    'A': 5,
    'B': 7,
    'C': 9,
    'D': 10
}

QUANTUM = 5 # pode ser alterado, não estabelecido

## essa função limita a parcela de tempo, então se o processo entar  no tempo, sera menor valor 
'''def tempo_quantum (quantum, valor_min = 1, valor_max= 5 ):
  if (quantum < valor_min ):
    return valor_min
  elif (quantum > valor_min): 
    return valor_max 
  else: 
    return quantum
  '''

