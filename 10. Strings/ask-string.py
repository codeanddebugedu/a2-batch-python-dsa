"""
Enter a string = Python is great
Enter a string = xyz xyz xyz
Enter a string = 1234
Enter a string = q

Python is great
xyz xyzx xyz
1234
"""

result = ""

while True:
    s = input("Enter your sentence = ")  # PYTHON is GReat
    # if s == "q" or s == "Q":
    #     break
    if s.lower() == "q":
        break
    result += s
    result += "\n"

print(result[:-1])


# result += "python"  # result = result + "python"
# result += "is"
# result += "good"
# print(result)
