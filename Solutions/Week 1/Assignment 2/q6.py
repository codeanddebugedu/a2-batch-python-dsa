"""
Ask 4 numbers from user. Make sure all the numbers entered by user are dierent. 
Print which number is the smallest.
"""

# If you are using multiple AND conditions that is also OK

num1: int = int(input("Enter number 1: "))
num2: int = int(input("Enter number 2: "))
num3: int = int(input("Enter number 3: "))
num4: int = int(input("Enter number 4: "))

smallest = num1

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num4 < smallest:
    smallest = num4

print(f"The smallest number = {smallest}")
