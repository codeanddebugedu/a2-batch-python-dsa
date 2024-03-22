"""
Make a function which takes filename as a parameter. 
Return the number of lines present in that file.
"""


def countLines(filename: str) -> int:
    try:
        """
        Method 1
        file = open(filename, 'r')
        line_count = 0
        for line in file:
            line_count += 1
        file.close()
        return line_count
        """
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return len(lines)
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to show user there is an error


filename = "hello.txt"
line_count = countLines(filename)
if line_count != -1:
    print(f"Number of lines in {filename} = {line_count}")
