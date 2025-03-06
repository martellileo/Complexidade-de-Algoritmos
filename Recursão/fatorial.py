import time

def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

start = time.time()
fatorial_iterativo(50)
end = time.time() - start
print(f"iterativo - {end*1000} ms")

start = time.time()
fatorial_recursivo(50)
end = time.time() - start
print(f"recursivo - {end*1000} ms")