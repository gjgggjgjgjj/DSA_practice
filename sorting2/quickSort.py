#from mergeSort import randomList


def quicksort(A):
    # calls the recursive version with modified = False
    return quicksortR(A, 0, len(A) - 1, False) #again this return work


def modified_quicksort(A):
    #the test case with the professor
    return quicksortR(A, 0, len(A) - 1, True) #this returns work


def quicksortR(A, low, high, modified):
    work = 0

    work +=1
    if low >= high:
        return work

    work += 1
    if modified:
        work += 3
        mid = (low + high) // 2
        A[low], A[mid] = A[mid], A[low]

    pivot = A[low]
    pivot_index = low

    # move all items < pivot to the left side
    for i in range(low + 1, high + 1):

        work += 1
        if A[i] < pivot:
            work += 2
            pivot_index += 1
            A[pivot_index], A[i] = A[i], A[pivot_index]

    # put pivot in its final position
    work += 1
    A[low], A[pivot_index] = A[pivot_index], A[low]

    #left and right like in mergesort
    left_work = quicksortR(A, low, pivot_index - 1, modified)

    right_work = quicksortR(A, pivot_index + 1, high, modified)

    work += left_work + right_work
   
    return work
    #one pass of the quickSort
    #the first pass we do index 1 NOT 0
    #then we go including the last one
    """
    somevar showing left most index    
    leftptr = low+1
    for loop:
        compare left and right 
        some if(): comparing to switch one at a time
            swap
            leftptr += 1

    pivot = leftptr -1
    quickSort(A[leftptr:rightptr])  #some recursion after this is one pass
    quickSort[rightptr:]
    
    return
    """

def main():
    testlist00 = randomList(15)
    testlist01 = randomList(15)
    testlist02 = randomList(100)

    print("Here are lists that we will test \n",testlist00,"\n", testlist01,"\n", testlist02)
    print("\n-----------------------------------\nHere is both sorted using quickSort")
    quicksort(testlist00)
    quicksort(testlist01)
    quicksort(testlist02)

    print(testlist00)
    print(testlist01)
    print(testlist02)
    print("\n\n================================================================\nHere type a number for a list length that you wanna test")
    leLen = int(input("---> "))
    leLenList = randomList(leLen)
    print("\n--------\nHere is your list", leLenList)

    quicksort(leLenList)
    print("\n\n\n\n\n\n\n\n\n\n\n\n------\n-----\n-----\n\n-----\nHere is it sorted in quickSort\n-----\n",leLenList)

if __name__ == "__main__":
    main()

