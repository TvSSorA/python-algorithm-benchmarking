def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1

            if j > i:
                arr[i], arr[j] = arr[j], arr[i]
    
    return i

def quickSort(arr: list[int], low: int, high: int) -> list[int]:
     if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
