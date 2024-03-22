"""
Make a function which takes filename as a parameter. 
Return the count of words which end with e.

Example (File Content)
python is great
this is a great course
we are doing dsa

OUTPUT
2
"""


def countWords(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        words = data.split()
        count = 0
        for word in words:
            if word.endswith("e") or word.endswith("E"):
                count += 1
        return count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "hello.txt"  # Replace with the name of your file
word_count = countWords(filename)
if word_count != -1:
    print(f"Count of words ending with 'e' = {word_count}")
