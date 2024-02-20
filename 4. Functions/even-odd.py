"""
Make a function named checkOddEven
Which take 1 integer as a argument

If integer is Even, then Return True
else return False
"""

# def checkOddEven(num: int) -> bool:
#     if num % 2 == 0:
#         return True
# return False


def checkOddEven(num: int) -> bool:
    return num % 2 == 0


checkOddEven(10)
