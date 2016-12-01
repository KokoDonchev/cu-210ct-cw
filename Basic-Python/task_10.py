L = [1, 6, 8, 1, 5, 6, 8, 1, 6, 7, 1, 3]


def generateSubsequences(sequence):

    sequences = []
    temp = []
    for index in range(0, len(sequence) - 1):
        if (sequence[index] <= sequence[index + 1]):
            temp.append(sequence[index])
        else:
            temp.append(sequence[index])
            sequences.append(temp)
            temp = []

    temp.append(sequence[index + 1])
    sequences.append(temp)

    return highestSubsequence(sequences)

def highestSubsequence(sequences):
    items = 0
    biggestSequence = 0
    for subsquence in sequences:
        if len(subsquence) > items:
            items = len(subsquence)
            biggestSequence = subsquence

    return("Biggest sequence", biggestSequence)

print(generateSubsequences(L))
