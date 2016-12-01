"""
Week 4 Task 1

Adapt the binary search algorithm so that instead of outputting whether a specific value was found,
it outputs whether a value within an interval (specified by you) was found.
Write the pseudocode and code and give the time complexity of the algorithm using the Big O notation.

Example input: L = [2,3,5,7,9,13] low= 10 high = 14 Output: True

"""

def binarySearch(alist, start, end):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] >= start and alist[midpoint] <= end:
            found = True
        else:
            if high < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


L = [2, 3, 5, 7, 9, 13]
low = 10
high = 14
print(binarySearch(L, low, high))


# O(log n)