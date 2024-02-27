"""
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(i, end=" ")
    print()
