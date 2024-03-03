"""
Write a function named notPrimeNumbers which accepts 2 integers n1 and n2. 
Print all the numbers from n1 to n2 which are not prime.
"""


def is_prime(num: int) -> int:
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def notPrimeNumbers(n1: int, n2: int) -> None:
    for num in range(n1, n2 + 1):
        if not is_prime(num):
            print(num, end=" ")
    print()


notPrimeNumbers(1, 10)
notPrimeNumbers(5, 20)
