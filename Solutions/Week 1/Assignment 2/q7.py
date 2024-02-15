"""
Take Salary as input from User and Update the salary of an employee

salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""

salary: float = float(input("Enter the salary =  "))

if salary < 10000:
    increment = 5
elif 10000 <= salary < 20000:
    increment = 10
elif 20000 <= salary < 50000:
    increment = 15
else:
    increment = 20

increment_amount = (increment / 100) * salary
new_salary = salary + increment_amount

print(f"The new salary = {new_salary:.2f}")
