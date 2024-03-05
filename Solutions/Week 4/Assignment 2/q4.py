"""
Generate a list of numbers less than 1000 which are 
divisible by the sum of their digits. (These were solved in contests)
"""
from typing import List


def sumOfDigits(n: int) -> int:
    total = 0
    while n > 0:
        last_digit = n % 10
        total = total + last_digit
        n = n // 10
    return total


def generateList(num: int) -> List[int]:
    return [i for i in range(1, num + 1) if i % sumOfDigits(i) == 0]


x = generateList(500)
print(x)
