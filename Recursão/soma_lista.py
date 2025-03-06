import time

def soma_lista_iterativa(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

def soma_lista_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista_recursiva(lista[1:])

start = time.time()
soma_lista_iterativa(range(900))
end = time.time() - start
print(f"iterativo - {end*1000} ms")

start = time.time()
soma_lista_recursiva(range(900))
end = time.time() - start
print(f"recursivo - {end*1000} ms")