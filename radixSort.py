from math import log10, floor

def radixSort(arr: list[int]) -> list[int]:
    res = []
    buckets = []

    for i in range(floor(log10(max(arr))) + 1):
        temp = [[], [], [], [], [], [], [], [], [], []]

        if len(buckets) == 0:
            for num in arr:
                temp[(num // 10**i) % 10].append(num)
            buckets = temp
        else:
            for bucket in buckets:
                for num in bucket:
                    temp[(num // 10**i) % 10].append(num)
                buckets = temp
    for bucket in buckets:
        res += bucket
    
    return res