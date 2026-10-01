#from bubblesort import createRandomList


def shakerSort(leList):
    work = 0

    looping = False
    #this is to break the looping
    exitcnt = 0
    while not looping:
        """
        if exitcnt > 1:
            print("on loop number",exitcnt)
        """


        looping = True
        for i in range(len(leList)-1):
            
            work += 1
            if leList[i] > leList[i+1]:
                looping = False

                work +=1
                leList[i], leList[i+1] = leList[i+1], leList[i]

        for i in range(len(leList)-1,0,-1):

            work += 1
            if leList[i] < leList[i-1]:

                work += 1
                leList[i], leList[i-1] = leList[i-1], leList[i]
                looping = False
        #exitcnt +=1

    return work

def main():
    testList10 = createRandomList(10)
    testList11 = createRandomList(30)
    print("Here is list one: ",testList10,"\nHere is list two: ", testList11)
    shakerSort(testList10)
    shakerSort(testList11)
    print("\n\nNow here is them sorted using shakersort\n",testList10,"\n",testList11)


if __name__ == "__main__":
    main()
