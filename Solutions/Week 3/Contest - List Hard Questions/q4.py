"""
Write a Python code to check if a list is a palindrome 
(reads the same forwards and backwards). Just print “YES” or “NO”
"""

from typing import List


def isPalindrome(lst: List) -> bool:
    for i in range(0, len(lst)):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True


print(isPalindrome([1, 2, 3, 4, 4, 3, 2, 1]))
print(isPalindrome([1, 2, 3, 4, 3, 2, 1]))
print(isPalindrome([1, 2, 3, 4, 3, 4, 1]))
