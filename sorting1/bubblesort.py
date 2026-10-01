import random
#buublesort goes from left to right
#shakersort goes left to right then after goes right to left
#then counting sort

def createRandomList(leLen):
    #making random range list for the amount of len
    #making a list to return
    leList = []
    for i in range(leLen):
        leList.append(random.randint(0,leLen-1))

    return leList

def BubbleSort(leList):
    #this is work to be tested for testingSort
    work = 0

    exitcnt = 0
    looping = False
    while not looping:
        """if exitcnt > 1:
            print("on loop #",exitcnt)
        """
        
        looping = True
        for i in range(len(leList)-1):

            work += 1
            if leList[i] > leList[i+1]:
                looping = False
                work +=1
                leList[i], leList[i+1] = leList[i+1], leList[i]
        #exitcnt += 1
    return work
            
def main():
    testList00 = createRandomList(9)
    testList01 = createRandomList(15)
    print("Test list 1 with 9 random # & Test list 2 with 15 random #\n\n", testList00)
    print("\n", testList01)
    print("-------------------------------------------------------------------------")

    BubbleSort(testList00)
    BubbleSort(testList01)

    print("Now here is both sorted using my bubblesort\n",testList00,"\n",testList01)

    testList02 = createRandomList(100)
    print("\n\n\nHere is one really long list before and after sorted\n----------------------------------------------------------")
    print(testList02)
    BubbleSort(testList02)
    print("\n\n\n",testList02)

if __name__ == "__main__":
    main()


