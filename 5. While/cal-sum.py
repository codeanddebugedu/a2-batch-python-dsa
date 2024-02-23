"""
Enter a number = 10
Enter a number = 10
Enter a number = 10
Enter a number = 10
Enter a number = 10
Enter a number = 10
Enter a number = 0

60
"""

total = 0
while True:
    number = int(input("Enter a number = "))
    if number == 0:
        break
    total += number

print(total)
