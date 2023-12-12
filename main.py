from algs import bubbleSort
from algs import mergeSort
import random
import time


def createRandomList(length):
    list = []
    for x in range(length):
        list.append(random.randrange(1000))
    return list


def main():
    print("Test randomized input")
    randomListToSort = createRandomList(10)
    randomLongListToSort = createRandomList(1000)

    #Test bubble sort with random list of 10 numbers
    start_time = time.time()
    sortedList = bubbleSort.bubbleSort(randomListToSort.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Bubblesort 10 elements --- %s milliseconds ---" % timeTosort)

    #Test bubble sort with random list of 1000 numbers
    start_time = time.time()
    longSortedList = bubbleSort.bubbleSort(randomLongListToSort.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Bubblesort 1000 elements --- %s milliseconds ---" % timeTosort)

    #Test merge sort with random list of 10 numbers
    start_time = time.time()
    mergeSort.Sort(randomListToSort.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Mergesort 10 elements --- %s milliseconds ---" % timeTosort)

    #Test merge sort with random list of 1000 numbers
    start_time = time.time()
    mergeSort.Sort(randomLongListToSort.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Mergesort 1000 elements --- %s milliseconds ---" % timeTosort)

    #######################################
    #SORTED LISTS
    #######################################
    print("\nTest best case (sorted list)")

    start_time = time.time()
    bubbleSort.bubbleSort(sortedList.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Bubblesort 10 elements --- %s milliseconds ---" % timeTosort)

    #Test bubble sort with random list of 1000 numbers
    start_time = time.time()
    bubbleSort.bubbleSort(longSortedList.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Bubblesort 1000 elements --- %s milliseconds ---" % timeTosort)

    #Test merge sort with random list of 10 numbers
    start_time = time.time()
    mergeSort.Sort(sortedList)
    timeTosort = (time.time() - start_time) * 1000
    print("Mergesort 10 elements --- %s milliseconds ---" % timeTosort)

    #Test merge sort with random list of 1000 numbers
    start_time = time.time()
    mergeSort.Sort(longSortedList.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Mergesort 1000 elements --- %s milliseconds ---" % timeTosort)

    reverseSortedList = sortedList.copy()
    reverseSortedList.reverse()
    reverseLongSortedList = longSortedList.copy()
    reverseLongSortedList.reverse()

    #######################################
    #REVERSE LISTS
    #######################################
    print("\nTest worst case (reverse sorted list)")

    start_time = time.time()
    bubbleSort.bubbleSort(reverseSortedList.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Bubblesort 10 elements --- %s milliseconds ---" % timeTosort)

    #Test bubble sort with random list of 1000 numbers
    start_time = time.time()
    bubbleSort.bubbleSort(reverseSortedList.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Bubblesort 1000 elements --- %s milliseconds ---" % timeTosort)

    #Test merge sort with random list of 10 numbers
    start_time = time.time()
    mergeSort.Sort(reverseLongSortedList.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Mergesort 10 elements --- %s milliseconds ---" % timeTosort)

    #Test merge sort with random list of 1000 numbers
    start_time = time.time()
    mergeSort.Sort(reverseLongSortedList.copy())
    timeTosort = (time.time() - start_time) * 1000
    print("Mergesort 1000 elements --- %s milliseconds ---" % timeTosort)



if __name__ == "__main__":
    main()