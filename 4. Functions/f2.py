"""
Make 4 functions - add, sub, div, mul
"""


def add():
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    print(f"Addition = {num1 + num2}")


def subtract():
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    print(num1 - num2)


def multiply():
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    print(num1 * num2)


def divide():
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    result = num1 / num2
    print(result)


add()
subtract()
multiply()
divide()
