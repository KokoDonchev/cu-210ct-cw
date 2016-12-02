""""
Week 1 Task 2

Count the number of trailing 0s in a factorial number.

"""


def factorial(number):

    """ Generate a factorial number """

    for i in range(1, number):
        number = number * i

    return number


def count(number):

    """
    Count the trailing zeros.
    Can be done in few way but this one is with parsing it to
    string and reversing it.

    """

    generate_factorial = factorial(number)
    trailing_zeros = 0

    for character in reversed(str(generate_factorial)):
        if character == '0':
            trailing_zeros += 1
        else:
            break

    return trailing_zeros


try:
    user_input = int(input("Enter a number: "))
    trailingZeros = count(user_input)
    print("In the number", user_input, "there", "is" if trailingZeros == 1 else "are", trailingZeros, "trailing", "zero" if trailingZeros == 1 else "zeros")
except ValueError:
    print("The input that you have entered is not an Integer")
