"""
Create a python function named isPalindrome which accepts a 
string as a parameter and return True if its a palindrome. 
Palindrome are words which is same when read from start and 
same when read from the end.
"""


def isPalindrome(string: str) -> bool:
    # Method 1
    lower_string = string.lower()
    reversed_string = lower_string[::-1]
    if string.lower() == reversed_string:
        return True
    return False

    # Method 2
    """
    return string.lower() == string[::-1].lower()
    """


print(isPalindrome("Mom"))
