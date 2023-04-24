from math import ceil
from radixSort import radixSort

def bucketSort(arr):
    bucketSize = 5
    bucketCount = ceil(len(arr) / bucketSize)

    buckets = [[] for _ in range(bucketCount)]

    for num in arr:
        buckets[ceil(num / bucketSize) - 1].append(num)
    
    for i in range(len(buckets)):
        buckets[i] = radixSort(buckets[i])
    
    res = []
    for bucket in buckets:
        res += bucket

    return res
