"""
Week 3 Task 2

Write a recursive function (pseudocode and code) to check if a number n
is prime (hint: check whether nis divisible by any number below n).

"""

def checkPrime(number, i = 2):
    if i == number:
        return "Number is prime"
    else:
        if number % i == 0:
            return "Number is not prime"
        return checkPrime(number, i + 1)


print(checkPrime(10))