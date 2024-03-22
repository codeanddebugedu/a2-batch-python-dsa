"""
Make a function which takes filename as a parameter. 
Return the number of words present in that file.
"""


def countWords(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        word_count = len(data.split())
        file.close()
        return word_count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to show user there is an error


file_name = "hello.txt"
word_count = countWords(file_name)
if word_count != -1:
    print(f"Number of words in {file_name} = {word_count}")
