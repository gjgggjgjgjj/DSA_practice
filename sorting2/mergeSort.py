import random 

def randomList(num):
    randList = []
    for i in range(num - 1):
        randnum = random.randint(0,num - 1)
        randList.append(randnum)
    return randList
    
#lovely recursion
def merge_sort(A):
    work = 0   #this is for testingSort

    #list is sorted
    if len(A) <= 1:
        return work

    # Split A into L and R
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    # Recursively sort both halves
    left_work = merge_sort(L)
    right_work = merge_sort(R)
    work += left_work + right_work

    # Merge the two sorted halves back into A
    i = 0   # index into L
    j = 0   # index into R
    k = 0   # index into A

    # Merge while both lists have items
    # have to always remember that A is just the last list that we split from 
    # so at the bottom it's just 2 items in a list with l & r being 2 from that list
    # so again remember that deeply recursed we are only viewing a few items
    while i < len(L) and j < len(R):
        work +=1
        if L[i] <= R[j]:
            work +=1
            A[k] = L[i]
            i += 1
        else:
            work +=1
            A[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining items from L
    # took a sec to implement this as we forgot that sometimes with odd numbers the split has one
    # finishing earlier
    while i < len(L):
        work +=1
        A[k] = L[i]
        i += 1
        k += 1

    #same for right list
    while j < len(R):
        work += 1
        A[k] = R[j]
        j += 1
        k += 1

    return work
        
def main():
    testlist00 = randomList(15)
    testlist01 = randomList(15)
    testlist02 = randomList(100)

    print("Here are lists that we will test \n",testlist00,"\n", testlist01,"\n", testlist02)
    print("\n-----------------------------------\nHere is both sorted using merge sort")
    merge_sort(testlist00)
    merge_sort(testlist01)
    merge_sort(testlist02)

    print(testlist00)
    print(testlist01)
    print(testlist02)
    print("\n\n================================================================\nHere type a number for a list length that you wanna test")
    leLen = int(input("---> "))
    leLenList = randomList(leLen)
    print("\n--------\nHere is your list", leLenList)

    merge_sort(leLenList)
    print("\n\n\n\n\n\n\n\n\n\n\n\n------\n-----\n-----\n\n-----\nHere is it sorted in merge_sort\n-----\n",leLenList)

if __name__ == "__main__":
    main()








