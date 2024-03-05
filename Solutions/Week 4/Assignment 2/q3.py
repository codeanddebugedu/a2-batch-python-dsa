"""
Write a Python program to generate a list of prime numbers
less than 500 using list comprehension.
"""
from typing import List


def checkPrime(n: int) -> bool:
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    return factors == 2


def generatePrimeList(num: int) -> List[int]:
    return [i for i in range(1, num + 1) if checkPrime(i)]


x = generatePrimeList(500)
print(x)
