"""
Week 3 Task 1

Write the pseudocode and code for a function that reverses the words
in a sentence.
Input: "This is awesome"
Output: "awesome is This". Give the Big O notation.

bigO: O(n) - as n is number of characters in the string

Pseudocode

REVERSE-WORDS(string)
    temp <- ""
    final <- ""

    for character in string
        if character is not " "
            temp <- temp + character
        else
            final <- temp + " " + final
            temp = ""

    final <- temp + " " + final

    return final

"""

def reverseWords(string):

    temp = ""
    final = ""

    for char in string:
        if char != " ":
            temp += char
        else:
            final = temp + ' ' + final
            temp = ""

    final = temp + ' ' + final

    return final

print(reverseWords("This is awesome"))