number = int(input("Enter a number = "))

total = 0
while number > 0:
    last_digit = number % 10
    total = total + last_digit
    number = number // 10

print(total)
