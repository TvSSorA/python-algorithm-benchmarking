from bubbleSort import bubbleSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from radixSort import radixSort
from quickSort import quickSort
from shellSort import shellSort
from mergeSort import mergeSort
from countingSort import countingSort
from bucketSort import bucketSort

from random import shuffle
from timeit import default_timer
from numpy import format_float_positional

testData = [i for i in range(1, 10001)]
shuffle(testData)

clone = testData[::]


results = {}            

def sortThem(algo):
    startTime = default_timer()
    res = algo(clone)
    
    results[algo.__name__] = format_float_positional(default_timer() - startTime, trim="-")

    if res != sorted(clone): 
        print(f"{algo.__name__}: Sort failure!")
    if len(res) != len(clone): 
        print(f"{algo.__name__}: Length mismatch!")

def main():
    sortThem(bucketSort)
    sortThem(radixSort)
    sortThem(countingSort)
    print(results)

if __name__ == '__main__':
    main()