"""
Calculate the cube of all numbers from 1 to a given number.
"""


def cube_of_numbers(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total = total + (i**3)
    return total


print(cube_of_numbers(10))
print(cube_of_numbers(5))
