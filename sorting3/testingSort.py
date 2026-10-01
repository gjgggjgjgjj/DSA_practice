import sys
import os 

#adding parent directory
sys.path.append(os.path.abspath(".."))

from sorting1.countingSort import countingSort
from sorting1.bubblesort import BubbleSort, createRandomList
from sorting1.shakersort import shakerSort
from sorting2.mergeSort import merge_sort
from sorting2.quickSort import quicksort, modified_quicksort
import randomUnique
import random
import math



def printResults(sorts):

    workDone = []
    leLineOfFunctions = ""
    #data will be 2^n and that's how we'll test them
    upper = 3
    nsquare = 2**upper

    #to run random data at different lengths
    for powers in range(10):
        upper += 1
        nsquare = 2**upper
        #running the data through each function
        curWork = []
        for i in range(len(sorts)):
            leList = createRandomList(nsquare)
            curWork.append(sorts[i](leList))

        workDone.append(curWork)



    #finally printing
    for func in sorts:
        leLineOfFunctions += func.__name__ + " "
    print("  ",leLineOfFunctions)
    for data in workDone:
        line = ""
        for i in data:
            line += str(i) + " "
        print(line)





#make a function that berily makes a list not sorted (like swap first with the last)

#make main printing the time it took for each algorithm

def main():
    sorts = [BubbleSort,countingSort,shakerSort,merge_sort,quicksort,modified_quicksort] #the sorting functions
    #two nested loops for printing the results in log2 form 
    """
    print(s, endd=" ") #row
    for s in range(3,13):
        size = 2**5
        for sort in sorts:
            A = CreateRandomList(size) #make this the mostly sorted list after the first time
            work = sort(A)
            work = log(work,2)
            print(work,end="")
        print()  #new line
    """
    #gonna run data into each data set
    printResults(sorts)


if __name__ == "__main__":
    main()

