"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(6 - j, end=" ")
    print()
