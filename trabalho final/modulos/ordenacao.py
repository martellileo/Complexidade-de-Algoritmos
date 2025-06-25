import time
import random

def gerar_vetor(tipo, tamanho):
    if tipo == "aleatoria":
        return [random.randint(0, 1000) for _ in range(tamanho)]
    elif tipo == "crescente":
        return list(range(tamanho))
    elif tipo == "decrescente":
        return list(range(tamanho, 0, -1))
    elif tipo == "quase":
        vetor = list(range(tamanho))
        for i in range(0, tamanho, max(1, tamanho // 10)):
            if i + 1 < tamanho:
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
        return vetor
    else:
        raise ValueError("Tipo inválido")

def bubble_sort(v, passo=False):
    n = len(v)
    for i in range(n):
        for j in range(0, n - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                if passo:
                    print(v)
    return v

def selection_sort(v, passo=False):
    n = len(v)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if v[j] < v[min_idx]:
                min_idx = j
        v[i], v[min_idx] = v[min_idx], v[i]
        if passo:
            print(v)
    return v

def insertion_sort(v, passo=False):
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0 and chave < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave
        if passo:
            print(v)
    return v

def merge_sort(v, passo=False):
    if len(v) > 1:
        mid = len(v) // 2
        L = v[:mid]
        R = v[mid:]

        merge_sort(L, passo)
        merge_sort(R, passo)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                v[k] = L[i]
                i += 1
            else:
                v[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            v[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            v[k] = R[j]
            j += 1
            k += 1
        if passo:
            print(v)
    return v

def quick_sort(v, passo=False):
    def _quick_sort(v, low, high):
        if low < high:
            pi = partition(v, low, high)
            _quick_sort(v, low, pi - 1)
            _quick_sort(v, pi + 1, high)

    def partition(v, low, high):
        pivot = v[high]
        i = low - 1
        for j in range(low, high):
            if v[j] <= pivot:
                i += 1
                v[i], v[j] = v[j], v[i]
                if passo:
                    print(v)
        v[i + 1], v[high] = v[high], v[i + 1]
        if passo:
            print(v)
        return i + 1

    _quick_sort(v, 0, len(v) - 1)
    return v

def heap_sort(v, passo=False):
    def heapify(v, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and v[l] > v[largest]:
            largest = l
        if r < n and v[r] > v[largest]:
            largest = r

        if largest != i:
            v[i], v[largest] = v[largest], v[i]
            if passo:
                print(v)
            heapify(v, n, largest)

    n = len(v)
    for i in range(n // 2 - 1, -1, -1):
        heapify(v, n, i)
    for i in range(n - 1, 0, -1):
        v[i], v[0] = v[0], v[i]
        if passo:
            print(v)
        heapify(v, i, 0)
    return v

def ordenacao():
    print("\nOrdenação")
    tipo = input("Tipo -> aleatoria | crescente | decrescente | quase): ").strip().lower()
    tamanho = int(input("Tamanho do vetor: "))
    passo = input("Visualizar passo a passo (s/n)? ").strip().lower() == 's'

    vetor = gerar_vetor(tipo, tamanho)

    print(  "\n[1] Bubble Sort\n"
            "[2] Selection Sort\n"
            "[3] Insertion Sort\n"
            "[4] Merge Sort\n"
            "[5] Quick Sort\n"
            "[6] Heap Sort\n"
            "[0] Voltar")
    metodo = input("Escolha o método: ").strip()

    metodos = {
        '1': bubble_sort,
        '2': selection_sort,
        '3': insertion_sort,
        '4': merge_sort,
        '5': quick_sort,
        '6': heap_sort
    }

    if metodo in metodos:
        func = metodos[metodo]
        inicio = time.time()
        resultado = func(vetor.copy(), passo)
        tempo = time.time() - inicio
        print("Vetor ordenado:", resultado)
        print("Tempo de execução:", tempo)
    elif metodo == '0':
        return
    else:
        print("Método inválido")