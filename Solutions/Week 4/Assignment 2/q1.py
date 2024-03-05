"""
Write a Python program to generate a list of powers of 2 less
than 100 using list comprehension
"""

from typing import List
from math import sqrt


def generatePowerList(num: int) -> List[int]:
    # return [2**i for i in range(0, num) if 2**i < num]
    return [
        2**i for i in range(0, int(sqrt(num)) + 1) if 2**i < num
    ]  # More optimal


x = generatePowerList(8)
print(x)
