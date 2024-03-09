"""
Make a password strength function. It will accept a string from user. 
Return True if it is a strong password.Strong password has these characteristics.
Minimum 8 character
Minimum 1 uppercase alphabet
Minimum 1 lowercase alphabet
Contains at least 1 special symbol (any symbol)
Minimum 1 digit
"""


def isStrongPassword(password: str):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if (
        len(password) >= 8
        and has_uppercase
        and has_lowercase
        and has_digit
        and has_special
    ):
        return True
    else:
        return False


password = input("Enter a password: ")
print(isStrongPassword(password))
