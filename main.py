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
    print("Sup negos")
    
    #Test bubble sort with random list of 10 numbers
    listToSort = createRandomList(10)
    print(listToSort)
    start_time = time.time()
    sortedList = bubbleSort.bubbleSort(listToSort)
    print("--- %s seconds ---" % (time.time() - start_time))  
    print(sortedList)
    
    #Test bubble sort with random list of 1000 numbers
    LongListToSort = createRandomList(1000)
    print(LongListToSort)
    start_time = time.time()
    sortedList = bubbleSort.bubbleSort(LongListToSort)
    print("--- %s seconds ---" % (time.time() - start_time))  
    print(sortedList)
    
    #Test merge sort with random list of 10 numbers
    listToSort = createRandomList(10)
    print(listToSort)
    start_time = time.time()
    sortedList = mergeSort.Sort(listToSort)
    print("--- %s seconds ---" % (time.time() - start_time))  
    print(sortedList)
    
    #Test merge sort with random list of 1000 numbers
    LongListToSort = createRandomList(1000)
    print(LongListToSort)
    start_time = time.time()
    sortedList = mergeSort.Sort(LongListToSort)
    print("--- %s seconds ---" % (time.time() - start_time))  
    print(sortedList)

if __name__ == "__main__":
    main()