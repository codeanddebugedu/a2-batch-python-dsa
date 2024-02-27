"""
        *
      * *
    * * *
  * * * *
* * * * *
"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()
