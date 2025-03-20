def merge_sort_visual(arr, depth=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        print(f"{'  ' * depth}Dividindo: {arr} -> {left_half} | {right_half}")

        merge_sort_visual(left_half, depth + 1)
        merge_sort_visual(right_half, depth + 1)

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

        print(f"{'  ' * depth}Mesclando: {arr}")

# Lista para testar
arr = [8, 3, 5, 2, 7, 6,10,20,99,67,48,78]
print("Lista original:", arr)
merge_sort_visual(arr)

print("Lista ordenada:", arr)