"""
Write a function divide that takes two numbers as input and returns their division. 
Call this function with invalid input arguments (e.g., strings instead of numbers) 
and handle any exceptions that may occur.
"""


def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None
    except TypeError:
        print("Invalid input type. Please provide numeric values.")
        return None


result1 = divide(10, 0)
print(f"Result 1 = {result1}")

result2 = divide("a", 5)
print(f"Result 2 = {result2}")
