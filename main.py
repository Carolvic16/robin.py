import threading 
import time 
from threading import Event, Thread 


## essa função limita a parcela de tempo, então se o processo entar  no tempo, sera menor valor 
def tempo_quantum (quantum, valor_min = 1, valor_max= 5 ):
  if (quantum < valor_min ):
    return valor_min
  elif (quantum > valor_min): 
    return valor_max 
  else: 
    return quantum