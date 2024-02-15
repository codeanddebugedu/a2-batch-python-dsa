"""
Write a program to calculate bill. 
Ask the final amount from the user.
You have to give discount and print the final bill after discount.

50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount

Print the discount and the final amount to be paid.
Example 1
Enter bill amount = 80000
You got 30% discount
Your final bill is Rs. 56000
"""

bill_amount: float = float(input("Enter the bill amount: "))

if bill_amount >= 50000:
    discount_percentage = 30
elif 40000 <= bill_amount < 50000:
    discount_percentage = 25
elif 30000 <= bill_amount < 40000:
    discount_percentage = 20
elif 10000 <= bill_amount < 30000:
    discount_percentage = 10
else:
    discount_percentage = 0

discount_amount: float = (discount_percentage / 100) * bill_amount
final_amount: float = bill_amount - discount_amount

print(f"You got {discount_percentage}% discount")
print(f"Your final bill is Rs. {final_amount:.2f}")
