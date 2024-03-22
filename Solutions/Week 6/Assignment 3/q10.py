"""
Print each line of the file in reverse order.
Example (File Content)
python is great
this is a great course
we are doing dsa

OUTPUT
great is python
course great a is this
dsa doing are we
"""


def printLines(filename: str) -> None:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            words = line.strip().split()
            reversed_words = words[::-1]
            reversed_line = " ".join(reversed_words)
            print(reversed_line)
    except FileNotFoundError:
        print("File not found!")


filename = "hello.txt"
printLines(filename)
