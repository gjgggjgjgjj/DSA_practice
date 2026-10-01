import random

def createUniqueRandomList(size):
    A = []

    while len(A) < size:
        r = random.randint(0, size -1)
        if r not in A:   #this is another loop hidden
            A.append(r)

    return A

def main():
    deck = createUniqueRandomList(52)
    print(deck)


if __name__ == "__main__":
    main()
