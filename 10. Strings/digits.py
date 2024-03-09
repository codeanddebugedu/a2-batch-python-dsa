"""
Enter a = python123
Enter b = good22

python123good22


Enter a = 50
Enter b = 20

70
"""


def add(string1: str, string2: str) -> str | int:
    if string1.isdigit() and string2.isdigit():
        return int(string1) + int(string2)
    return string1 + string2


print(add("python", "good"))
print(add("70", "40"))
