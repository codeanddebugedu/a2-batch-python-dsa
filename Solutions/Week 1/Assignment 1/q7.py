"""
Check if the number entered by User is divisible by 3 or not
"""

number = int(input("Enter a number: "))

if number % 3 == 0:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 3.")
