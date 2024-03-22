"""
Make a function which takes filename as a parameter. 
Print the words in that file which has length greater than 4. 
"""


def printWords(filename: str) -> None:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            words = line.strip().split()
            for w in words:
                if len(w) > 4:
                    print(w, end=" ")
            print()  # Print a newline after printing all words
    except FileNotFoundError:
        print("File not found!")


filename = "hello.txt"
printWords(filename)
