import time
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # print(f"{arr}")
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # print(f"{arr}")
    return arr

def inserction_sort(arr):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    # print(f"{arr}")
    return arr

def sorts(n):
    print(f"\n")
    print(f"---------------------------------------------------------")
    print(f"{n}")
    print(f"---------------------------------------------------------")

    array = np.random.rand(n)
    start = time.time()
    bubble_sort(array)
    end = time.time() - start
    print(f"bubble sort \t{end}")

    array = np.random.rand(n)
    start = time.time()
    selection_sort(array)
    end = time.time() - start
    print(f"selection sort \t{end}")

    array = np.random.rand(n)
    start = time.time()
    inserction_sort(array)
    end = time.time() - start
    print(f"inserction sort {end}")
    print(f"---------------------------------------------------------")

sorts(10)
sorts(100)
sorts(1000)
sorts(10000)
sorts(100000)