from collections import deque
import time

def comparar_fila_lista():
    fila = deque()
    start_time = time.time()
    for i in range(100000):
        fila.append(i)
    while fila:
        fila.popleft()
    fila_time = time.time() - start_time

    lista = []
    start_time = time.time()
    for i in range(100000):
        lista.append(i)
    for i in lista:
        lista.remove(i)
    lista_time = time.time() - start_time

    print(f"Tempo de operação na fila: {fila_time}")
    print(f"Tempo de operação na lista: {lista_time}")

comparar_fila_lista()
