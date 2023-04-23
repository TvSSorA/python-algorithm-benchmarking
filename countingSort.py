def countingSort(arr: list[int]) -> list[int]:
    highest = max(arr)

    counts = [0 for _ in range(highest + 1)]
    for num in arr:
        counts[num] += 1
    
    for i in range(len(counts)):
        counts[i] += counts[i - 1]
    
    for j in range(len(counts) - 1, 0, -1):
        counts[j] = counts[j - 1]
    counts[0] = 0
    
    sorted = [0 for _ in range(len(arr))]
    for num in arr:
        idx = counts[num]
        sorted[idx - 1] = num
        counts[num] += 1

    return sorted 