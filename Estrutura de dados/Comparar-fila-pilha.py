from collections import deque
import time

def comparar_fila_pilha():
    pilha = []
    start_time = time.time()
    for i in range(100000):
        pilha.append(i)
    while pilha:
        pilha.pop()
    pilha_time = time.time() - start_time

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
    while lista:
        lista.pop(0)
    lista_time = time.time() - start_time

    print(f"Tempo de operação na pilha: {pilha_time*1000}ms")
    print(f"Tempo de operação na fila: {fila_time*1000}ms")
    print(f"Tempo de operação na lista: {lista_time*1000}ms")

comparar_fila_pilha()
