def selectionSort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        lowest = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j

        if lowest != i:
            arr[i], arr[lowest] = arr[lowest], arr[i]

    return arr