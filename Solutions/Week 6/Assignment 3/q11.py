"""
Print each word of the file in reverse order.
Example (File Content)
python is great
this is a great course
we are doing dsa

OUTPUT
nohtyp si taerg
siht si a taerg esruoc
ew era gniod asd
"""


def printWordsInReverse(filename: str) -> None:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            words = line.strip().split()
            reversed_words = [word[::-1] for word in words]
            print(" ".join(reversed_words))
    except FileNotFoundError:
        print("File not found!")


filename = "hello.txt"
printWordsInReverse(filename)
