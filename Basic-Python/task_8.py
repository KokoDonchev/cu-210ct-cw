"""
Week 3 Task 3

Write a recursive function (pseudocode and code) that removes all vowels from a given string.
Input: "beautiful" Output: "btfl".

"""


def removeVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word:
        if word[0] in vowels:
            # in case there is a vowel, we remove it
            return ("" + removeVowels(word[1:]))
        else:
            # in case the current first character in the word is not a vowel, we keep it
            return (word[0] + removeVowels(word[1:]))
    else:
        return ("")


print(removeVowels("beautiful"))