"""
Make a class named area

There are no attributes related to area.

But it should have 4 methods, rectange, square, circle, triangle

rectangle
l,b -> input

square
s -> input

circle
r -> parameter

triangle
b,h -> parameter

obj=Area()
obj.rectangle()
obj.circle(34)
"""

import math


class Area:
    def rectangle(self) -> None:
        length = float(input("Enter a length: "))
        breadth = float(input("Enter a breadth: "))
        print(length * breadth)

    def square(self) -> None:
        side = float(input("Enter a side: "))
        print(side**2)

    def circle(self, radius=0) -> float:
        area = 2 * math.pi * radius
        return area

    def triangle(self, breadth=0, height=0) -> None:
        area = 0.5 * breadth * height
        print(area)


object = Area()
print(object.circle(8))
object.rectangle()
object.square()
object.triangle(5, 6)
