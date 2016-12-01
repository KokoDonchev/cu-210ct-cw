"""
Week 2 Task 1

Write the pseudocode for a function which returns the highest perfect square which is less or equal to its parameter
(a positive integer). Implement this in a programming language of your choice.


Pseudocode

Perfect-Square(number)
    i <- 0
    while i * i is less or equal to number
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
    i -= 1  # preparing to multiply the previous number by itself because we need the closest lower number
    return i * i

try:
    user_input = int(input("Enter a number: "))
    print("Higher possible square for", user_input, "is", highestPerfectSquare(user_input))
except ValueError:
    print("The input that you have entered is not an Integer")
