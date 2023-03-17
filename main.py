from bubbleSort import bubbleSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from radixSort import radixSort
from quickSort import quickSort
from shellSort import shellSort

from random import shuffle
from timeit import default_timer
from numpy import format_float_positional

testData = [i for i in range(1, 10001)]
results = {}            

def sortThem(algo):
    shuffle(testData)
    

    startTime = default_timer()
    res = algo(testData)
    
    results[algo.__name__] = format_float_positional(default_timer() - startTime, trim="-")

    if res != sorted(testData): 
        print(f"{algo.__name__}: Sort failure!")
    if len(res) != len(testData): 
        print(f"{algo.__name__}: Length mismatch!")

def main():
    sortThem(bubbleSort)
    sortThem(insertionSort)
    sortThem(selectionSort)
    sortThem(shellSort)
    sortThem(radixSort)
    print(results)

if __name__ == '__main__':
    main()