def circle(radius: float) -> float:
    return 3.14 * radius * radius


def rectangle(length: float, breadth: float) -> None:
    print(length * breadth)


def triangle(base: float, height: float) -> float:
    return 0.5 * base * height


def square(side: float) -> float:
    return side**2


if __name__ == "__main__":
    print(square(100))
