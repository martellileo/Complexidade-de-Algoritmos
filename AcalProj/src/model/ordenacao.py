import time as t




def bubble_sort(lista:list, tamanho:int, mostrar_passos:bool=False):
    tini = t.time()
    for i in range(tamanho):
        swapped = False
        for j in range(0, tamanho-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swapped = True
                if mostrar_passos:
                    print(f"Passo {i*tamanho+j+1}: {lista}")
        if not swapped:
            break
    tfim = t.time()
    tempo_decorrido = tfim - tini
    return lista, tempo_decorrido


def selection_sort(lista:list, tamanho:int, mostrar_passos:bool=False):
    tini = t.time()
    for i in range(tamanho):
        min_idx = i
        for j in range(i+1, tamanho):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        if mostrar_passos:
            print(f"Passo {i+1}: {lista}")
    tfim = t.time()
    tempo_decorrido = tfim - tini
    return lista, tempo_decorrido

def insertion_sort(lista:list, tamanho:int, mostrar_passos:bool=False):
    tini = t.time()
    for i in range(1, tamanho):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
        if mostrar_passos:
            print(f"Passo {i}: {lista}")
    tfim = t.time()
    tempo_decorrido = tfim - tini
    return lista, tempo_decorrido

def merge_sort(lista:list, tamanho:int, mostrar_passos:bool=False):
    if tamanho > 1:
        mid = tamanho // 2
        L = lista[:mid]
        R = lista[mid:]

        merge_sort(L, len(L), mostrar_passos)
        merge_sort(R, len(R), mostrar_passos)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

        if mostrar_passos:
            print(f"Lista mesclada: {lista}")

    return lista



def quick_sort(lista:list, tamanho:int, mostrar_passos:bool=False):
    if tamanho <= 1:
        return lista

    pivot = lista[tamanho // 2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]

    if mostrar_passos:
        print(f"Dividindo: {lista} -> {left} + {middle} + {right}")

    return quick_sort(left, len(left), mostrar_passos) + middle + quick_sort(right, len(right), mostrar_passos)

def heapify(lista, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lista[left] > lista[largest]:
        largest = left

    if right < n and lista[right] > lista[largest]:
        largest = right

    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        heapify(lista, n, largest)

def heap_sort(lista:list, tamanho:int, mostrar_passos:bool=False):
    tini = t.time()
    for i in range(tamanho // 2 - 1, -1, -1):
        heapify(lista, tamanho, i)

    for i in range(tamanho - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
        if mostrar_passos:
            print(f"Passo {tamanho-i}: {lista}")

    tfim = t.time()
    tempo_decorrido = tfim - tini
    return lista, tempo_decorrido

