"""
Make a function which takes filename as a parameter. 
Return the number of time the word the has appeared in that file.
"""


def wordOccurrences(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        words = data.split()

        word_count = 0
        for word in words:
            if word.lower() == "the":
                word_count += 1
        return word_count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "hello.txt"
count = wordOccurrences(filename)
if count != -1:
    print(f"The word 'the' appears {count} times in {filename}")
