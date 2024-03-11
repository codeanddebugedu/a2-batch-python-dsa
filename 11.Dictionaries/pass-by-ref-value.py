from typing import Dict


def greet(dictionary: Dict[str, int]) -> None:
    k = input("Enter key = ")
    v = int(input("Enter value = "))
    dictionary[k] = v


my_dict = {"anirudh": 77, "nihar": 11}
print(my_dict)

greet(my_dict)

print(my_dict)
