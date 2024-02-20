"""
Make 2 functions.
add() - it will take 3 integers - return the addition

checkOddEven() - it will take 1 integer, check if odd or even
"""


def checkOddEven(num: int) -> None:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def add(num1: int, num2: int, num3: int) -> int:
    total = num1 + num2 + num3
    return total


t = add(10, 20, 30)
print(t)
checkOddEven(t)
