import time
from functools import lru_cache

# iterativo
def fibonacci_iterativo(n):
    if n <= 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# recursivo
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

@lru_cache(None)
def fibonacci_memo(n):
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

start = time.time()
fibonacci_iterativo(30)
end = time.time() - start
print(f"iterativo - {end*1000} ms")

start = time.time()
fibonacci_recursivo(30)
end = time.time() - start
print(f"recursivo - {end*1000} ms")

start = time.time()
fibonacci_memo(30)
end = time.time() - start
print(f"memo - {end*1000} ms")