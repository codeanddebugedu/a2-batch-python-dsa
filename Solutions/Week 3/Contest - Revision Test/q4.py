"""
Write a Python program to check if a triangle is equilateral, 
isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides
"""


def checkTriangle(a: float, b: float, c: float):
    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"


a = float(input("Enter the length of side a = "))
b = float(input("Enter the length of side b = "))
c = float(input("Enter the length of side c = "))

if a + b > c and a + c > b and b + c > a:
    triangle = checkTriangle(a, b, c)
    print(f"Type of triangle is = {triangle}")
else:
    print("The given side lengths cannot form a triangle.")
