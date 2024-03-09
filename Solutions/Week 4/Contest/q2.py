"""
Keep asking characters from user until he presses q on the keyboard. 
Change all the capital letters to small, and all the small letters to capital.
"""

result = ""

while True:
    ch = input("Enter character = ")
    if ch == "q":
        break
    ascii_code = ord(ch)
    if 65 <= ascii_code <= 90:
        small_letter = chr(ascii_code + 32)
        result += small_letter
    elif 97 <= ascii_code <= 122:
        capital_letter = chr(ascii_code - 32)
        result += capital_letter
    else:
        result += ch

print(result)
