import time

# recursivo
def soma_recursiva(n):
    if n == 1:
        return 1
    return n + soma_recursiva(n - 1)

# iterativo
def soma_iterativa(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

start = time.time()
soma_iterativa(30)
end = time.time()
print(f"tempo de execucao: {(start-end)*1000} ms")

start = time.time()
soma_recursiva(30)
end = time.time()
print(f"tempo de execucao: {(start-end)*1000} ms")

