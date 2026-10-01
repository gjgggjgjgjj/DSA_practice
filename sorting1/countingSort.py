#from bubblesort import createRandomList

def countingSort(leList):
    work = 0   #this is for testingSort

    listLen = len(leList)
    
    work += 1
    hashOfNum = [0] * listLen
    returnList = []

    for i in leList:

        work += 2
        number = hashOfNum[i] + 1
        hashOfNum[i] = number

    for i in range(len(hashOfNum)):
        for a in range(hashOfNum[i]):
            work += 1
            returnList.append(i)


    work += 1
    leList[:] = returnList
    #print("during loop here is list\n", returnList)
    return work

def main():
    testList12 = createRandomList(15)
    print("Test list for counting sort:\n", testList12)
    print("\n---------------\nHere is it now sorted:\n")
    countingSort(testList12)
    print(testList12)


if __name__ == "__main__":
    main()
