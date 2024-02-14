"""
Take values of length and breadth of a rectangle from user and check if it is square or not.
"""

length = float(input("Enter the length of the rectangle = "))
breadth = float(input("Enter the breadth of the rectangle = "))

if length == breadth:
    print("It's a square.")
else:
    print("It's not a square.")
