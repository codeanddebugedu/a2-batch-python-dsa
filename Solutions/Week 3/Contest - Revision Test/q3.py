"""
Write a function named armstrongRange which accepts 2 integers n1 and n2. 
Print all the numbers from n1 to n2 which are armstrong numbers
"""


def is_armstrong(num: int) -> bool:
    result = 0
    temp = num
    while temp > 0:
        last_digit = temp % 10
        result = result + (last_digit**3)
        temp //= 10

    return result == num


def armstrongRange(n1: int, n2: int) -> None:
    for num in range(n1, n2 + 1):
        if is_armstrong(num):
            print(num)


armstrongRange(56, 1000)
