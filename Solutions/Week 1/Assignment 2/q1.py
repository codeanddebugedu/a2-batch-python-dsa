"""
Write a program that takes two numbers as input and checks 
if the first number is divisible by the second.
"""

num1: int = int(input("Enter number 1 = "))
num2: int = int(input("Enter number 2 = "))

if num1 % num2 == 0:
    print("Num1 is divisible by num2")
else:
    print("Num1 is not divisible by num2")
