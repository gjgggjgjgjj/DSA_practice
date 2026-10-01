import math
import os
import random
import sys

# Adding parent directory
sys.path.append(os.path.abspath(".."))

sys.setrecursionlimit(5000)

import randomUnique
from sorting1.bubblesort import BubbleSort, createRandomList
from sorting1.countingSort import countingSort
from sorting1.shakersort import shakerSort
from sorting2.mergeSort import merge_sort
from sorting2.quickSort import modified_quicksort, quicksort



def makeMostlySorted(size):
    swaps = 5
    A = list(range(size))

    for _ in (range(swaps)):
        i = random.randint(0, size -1)
        j = random.randint(0, size -1)

        A[i], A[j] = A[j], A[i]

    return A


def printResults(sorts):
    print("\nCounting work when sorting random data:")

    # Print table header
    header = f"{'':>4} " + " ".join(f"{func.__name__:>10}" for func in sorts)
    print(header)

    # Loop through sizes 2^3 (8) to 2^11 (2048)
    for k in range(3, 12):
        size = 2**k

        # Generate ONE base dataset for this size
        #change createRandomList if mostly sorted function to get data of it mostly sorted[]
        # base_list = createRandomList(size)
        base_list = makeMostlySorted(size)

        row_logs = []
        for func in sorts:
            # Pass a fresh copy of the base list to each algorithm
            data_copy = base_list.copy()
            work = func(data_copy)

            # Convert work to log2 (handling 0 safely)
            log_work = math.log2(max(1, work))
            row_logs.append(log_work)

        # Print formatted row: '03', '04', ... followed by log2 values
        row_str = f"{k:02d}   " + " ".join(f"{val:>10.2f}" for val in row_logs)
        print(row_str)


def main():
    sorts = [
        BubbleSort,
        shakerSort,
        countingSort,
        merge_sort,
        quicksort,
        modified_quicksort,
    ]
    printResults(sorts)


if __name__ == "__main__":
    main()
    
