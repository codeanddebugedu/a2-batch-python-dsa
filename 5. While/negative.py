"""
Ask a number from user = 50
-50 to 50

Ask a number from user = 10
-10 to 10

Ask a number from user = -13
13 to -13

Ask a number from user = -20
20 to -20
"""

number: int = int(input("Enter a number = "))  # -20
start = -number
end = number
if number > 0:
    while start <= end:
        print(start, end=" ")
        start += 1
else:
    while start >= end:
        print(start, end=" ")
        start -= 1
