"""
Ask 3 numbers from User and Calculate the Average
"""

n1 = int(input("Enter number 1 = "))
n2 = int(input("Enter number 2 = "))
n3 = int(input("Enter number 3 = "))

average = (n1 + n2 + n3) / 3

print(f"Average = {average}")
print(f"Average = {average:.2f}")  # To display output upto 2 decimals only
