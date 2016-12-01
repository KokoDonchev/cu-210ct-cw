""""
Week 1 Task 1

Write a function that randomly shuffles an array of integers and explain the rationale behind its implementation.

"""

from random import randrange

def shuffleArray(items):

    i = len(items)  # Getting the length of the array

    while i > 1:

        # reducing by 1 every iteration
        i = i - 1

        # generating a random index starting from 0 to the current iteration
        j = randrange(i)

        # swapping the position of the elements
        items[j], items[i] = items[i], items[j]

    return items


print(shuffleArray([1, 4, 9, 2, 8, 1, 4, 3]))
