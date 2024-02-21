"""
Ask M from user
Ask N from user


M to N

N to M

M=5
N=10
5 6 7 8 9 10

M=9
N=3
3 4 5 6 7 8 9
"""

m: int = int(input("Enter M = "))
n: int = int(input("Enter N = "))

if m < n:
    i = m
    while i <= n:
        print(i, end=" ")
        i += 1
else:
    i = n
    while i <= m:
        print(i, end=" ")
        i += 1
