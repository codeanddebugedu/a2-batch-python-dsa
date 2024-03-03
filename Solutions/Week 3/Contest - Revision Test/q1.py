"""
Calculate the cube of all numbers from 1 to a given number.
"""


# To just print the cubes
def print_cube_of_numbers(n: int) -> None:
    for i in range(1, n + 1):
        print(i**3, end=" ")
    print()


# To calculate sum of cubes
def cube_of_numbers(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total = total + (i**3)
    return total


print_cube_of_numbers(10)
print(cube_of_numbers(10))
