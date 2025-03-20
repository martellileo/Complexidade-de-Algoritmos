import time
import numpy as np

import matplotlib.pyplot as plt
import time

def plot_array(arr, pivot_index=None, title=""):
    plt.figure(figsize=(8, 4))
    colors = ['blue' if i != pivot_index else 'red' for i in range(len(arr))]
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.show()
    time.sleep(1)

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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivot_index = partition(arr, left, right)

        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)


def partition(arr, left, right):
    pivot = arr[right]  # Escolhendo o último elemento como pivô
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

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

    array = np.random.rand(n)
    start = time.time()
    merge_sort(array)
    end = time.time() - start
    print(f"merge sort \t{end}")

    array = np.random.rand(n)
    start = time.time()
    quick_sort(array)
    end = time.time() - start
    print(f"quick sort \t{end}")
    print(f"---------------------------------------------------------")

sorts(10)
sorts(100)
sorts(1000)
sorts(10000)
sorts(100000)