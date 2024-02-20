"""
3 requirements to get a certificate
1. Should be a part of C&D
2. Minimum class attended should be 20
3. Minimum assignment submitted = 45


Are you part of C&D = yes
Enter class attendted = 56
Enter assignment submitted = 68
You are eligible for certificate
"""

user_input = input("Are you a part of C&D: (yes/no)")
if user_input == "yes":
    user_input_class = int(input("Enter number of classes attended: "))
    if user_input_class >= 20:
        user_input_assignment = int(input("Enter number of assignments: "))
        if user_input_assignment >= 45:
            print("you're eligible for certificate")
        else:
            print("can't get certificate")
    else:
        print("can't get certificate")
else:
    print("can't get certificate")
