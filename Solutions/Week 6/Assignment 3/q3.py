"""
Make a function which takes filename as a parameter. 
Return the number of lines present in that file which does not start with T or t.
"""


def countLines(filename: str) -> int:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        count = 0
        for line in lines:
            if not line.strip().lower().startswith("t"):
                count += 1
        return count
    except FileNotFoundError:
        print("File not found!")
        return -1


filename = "hello.txt"
line_count = countLines(filename)
if line_count != -1:
    print(f"Number of lines in {filename} not starting with 'T' or 't' = {line_count}")
