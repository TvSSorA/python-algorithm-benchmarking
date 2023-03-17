def shellSort(arr: list[int]) -> list[int]:
    gap = len(arr) // 2

    while (gap > 0):
        for i in range(gap, len(arr)):
            j = i
            while j > 0 and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap -= 1
    
    return arr