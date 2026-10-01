from shakersort import shakerSort
from countingSort import countingSort
from bubblesort import createRandomList, BubbleSort


def main():
    testList000 = createRandomList(15)
    testList001 = createRandomList(15)
    testList002 = createRandomList(15)

    #bubblesort
    print("Here is a list before and after bubblesort\n------------------------------------------\n",testList000)
    BubbleSort(testList000)
    print("\nSorted:",testList000,"\n---------------------------------------------\n\n")

    #shakersort
    print("Here is a list before and after shakersort\n-----------------------------------------\n",testList001)
    shakerSort(testList001)
    print("\nSorted:",testList001,"\n-----------------------------------------\n\n")

    #countingSort
    print("Here is a list before and after countingSort\n----------------------------------------\n", testList002)
    countingSort(testList002)
    print("\nSorted:",testList002,"\n--------------------------------\n\n")
    
main()
