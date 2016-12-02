"""
Week 5 Task 1

Given a sequence of n integer numbers, extract the sub-sequence of
maximum length which is in ascending order.

"""

L = [1, 6, 1, 6, 9, 1, 6, 7, 8, 1, 3]


def generateSubsequences(sequence):

    sequences = [] # stores ALL sequences
    temp = [] # stores the sequence which the loop is checking

    for index in range(0, len(sequence) - 1): # -1 because we need next item
        if (sequence[index] <= sequence[index + 1]): # otherwise out of range err
            temp.append(sequence[index])
        else:
            temp.append(sequence[index])
            sequences.append(temp)
            temp = []

    temp.append(sequence[index + 1]) # because of the -1 we add the value here
    sequences.append(temp)

    return highestSubsequence(sequences)

def highestSubsequence(sequences):

    items = 0 # counts the item in the active sequence
    biggestSequence = [] # stores it until a bigger one is found

    for subsquence in sequences:
        if len(subsquence) > items:
            items = len(subsquence)
            biggestSequence = subsquence

    return("Biggest sequence", biggestSequence)

print(generateSubsequences(L))
