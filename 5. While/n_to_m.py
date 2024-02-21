"""
ASk M and N from user.
Print M to N.
"""

m: int = int(input("Enter M = "))
n: int = int(input("Enter N = "))

i: int = m
while i <= n:
    print(i, end=" ")
    i += 1
