import time

def func_a(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

def func_b(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

def func_c(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i], arr[j])

# -------------------------------------------------

def fibonacci_ineficiente(n):
    if n <= 1:
        return n
    return fibonacci_ineficiente(n - 1) + fibonacci_ineficiente(n - 2)

def fibonacci_iterativo(n):
    if n <= 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# -------------------------------------------------

def contar_pares_iguais(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                count += 1
    return count

def count_effi(nums):
    pares = []
    n = len(nums)
    for i in range(n):
        if nums[i] == nums[i]:
            pares.append((nums[i], nums[i]))
    return pares

arr = [1]
lista = [1, 2, 1, 2, 1]

print(f"----------------")
func_a(1)
print(f"----------------")
func_b(6)
print(f"----------------")
func_c(arr)
print(f"----------------")

inicio = time.time()
fibonacci_ineficiente(35)
fim = time.time() - inicio
print(f"Fibonnaci ineficiente - Tempo:", fim*1000, "ms")

inicio = time.time()
fibonacci_iterativo(35)
fim = time.time() - inicio
print(f"Fibonnaci iterativo - Tempo:", fim*1000, "ms")

print(f"----------------")

print(contar_pares_iguais(lista))
print(count_effi(lista))

# -------------------------------
# respostas:
# 1)
#   a)
#       A)
#           a) Melhor: O(1)
#           b) Meio: O(n²)
#           c) Pior: O(n²)
#       B)
#           a) Melhor: O(1)
#           b) Meio: O(N)
#           c) Pior: O(N)
#       C)
#           a) Melhor: O(1)
#           b) Meio: O(n²)
#           c) Pior: O(n²)
#
#   b) O terceiro algoritmo é melhor para entradas grandes, pois seu tempo de complexidade é O(N)
#
# 2)
#   a)  O(2^n)
#
#   b)  def fibonacci_iterativo(n):
#           if n <= 1: return 1
#           a, b = 0, 1
#           for _ in range(2, n + 1):
#               a, b = b, a + b
#           return b
#       Fibonnaci ineficiente - Tempo: 1165.2381420135498 ms
#       Fibonnaci iterativo - Tempo: 0.006198883056640625 ms
#
# 3)
#   a) O algoritmo possui complexidade O(n²) por conta de possuir dois laços alinhados:
#       for i in range(n):
#           for j in range(i+1, n):
#
#   b) (tentei)
#     def count_effi(nums):
#         pares = []
#         n = len(nums)
#         for i in range(n):
#             if nums[i] == nums[i]:
#                 pares.append((nums[i], nums[i]))
#         return pares