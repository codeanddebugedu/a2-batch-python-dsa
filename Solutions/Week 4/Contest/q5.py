"""
Ask a string from user. Replace all the space characters with “-”. 
Do not use replace() method.
"""


def replaceSpaces(string):
    result = ""
    for char in string:
        if char == " ":
            result += "-"
        else:
            result += char
    return result


user_string = input("Enter a string: ")

r = replaceSpaces(user_string)

print(r)
