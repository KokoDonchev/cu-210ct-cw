"""
Week 2 Task 1

Write the pseudocode for a function which returns the highest perfect square
which is less or equal to its parameter (a positive integer).
Implement this in a programming language of your choice.


Pseudocode

PERFECT-SQUARE(number)
    i <- 0
    while i * i <= number
        i <- i + 1
    i <- i - 1

    return i * i

"""


def highestPerfectSquare(number):

    """
    Generating the closest perfect square number which is less or equal
    to the number pulled from the user input
    """

    i = 0
    while i * i <= number:
        i += 1
    i -= 1  # to multiply the previous number by itself as we need the lower one
    return i * i

try:
    user_input = int(input("Enter a number: "))
    print("Higher possible square for", user_input, "is", highestPerfectSquare(user_input))
except ValueError:
    print("The input that you have entered is not an Integer")
