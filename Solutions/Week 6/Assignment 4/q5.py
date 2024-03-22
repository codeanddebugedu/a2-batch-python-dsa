import string


def generateFiles():
    try:
        for letter in string.ascii_uppercase:
            filename = letter + ".txt"
            with open(filename, "w") as file:
                pass
        print("Files created successfully.")
    except IOError:
        print("Error: An I/O error occurred.")


generateFiles()
