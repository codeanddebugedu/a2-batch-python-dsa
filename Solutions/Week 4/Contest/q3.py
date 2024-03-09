"""
Python Program to remove all duplicates from a given string
"""


def removeDuplicates(string):
    result = ""

    for char in string:
        if char not in result:
            result += char

    return result


string = "hheeelllooo"
print(removeDuplicates(string))
