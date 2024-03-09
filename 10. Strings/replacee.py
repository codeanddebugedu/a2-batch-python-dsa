def replaceChar(string: str) -> str:
    new_string: str = str()
    for char in string:
        if char.lower() == "i":
            new_string += "z"
        else:
            new_string += char
    return new_string


my_string: str = "delhi is clean city"
r = replaceChar(my_string)
print(r)
