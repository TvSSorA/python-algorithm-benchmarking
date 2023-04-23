def quickSort(arr: list[int]) -> list[int]:
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[-1]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
            
        return quickSort(less) + equal + quickSort(greater)
    else:
        return arr

def partition(arr: list[int], start: int, end: int) -> int:
    i, j = start, end
    pivot = arr[end]
    
    while (i < j):
        while (arr[i] < pivot):
            i += 1
        while (arr[j] > pivot):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return i 

def quicksortalt(arr: list[int], start: int, end: int):
    if start < end:
        pivot = partition(arr, 0, len(arr) - 1)
        quicksortalt(arr, start, pivot - 1)
        quicksortalt(arr, pivot + 1, end)   
    return arr