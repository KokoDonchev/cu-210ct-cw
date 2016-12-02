"""
Week 3 Task 3

Write a recursive function (pseudocode and code) that removes all vowels
from a given string.
Input: "beautiful" Output: "btfl".

Pseudocode

REMOVE-VOWELS(word)
    vowels <- [a, e, i, o, u]
    if word
        if word[0] in vowels
            return "" + REMOVE-VOWELS(word[1:])
        else
            return word[0] + REMOVE-VOWELS(word[1:])
    else
        return None

"""


def removeVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word:
        if word[0] in vowels:
            # there is a vowel, we remove it
            return ("" + removeVowels(word[1:]))
        else:
            # if first character in the word is not a vowel, we keep it
            return (word[0] + removeVowels(word[1:]))
    else:
        return ("")


print(removeVowels("beautiful"))