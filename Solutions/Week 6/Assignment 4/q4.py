def readLastNLines(filename: str, n: int) -> None:
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            total_lines = len(lines)
            if n > total_lines:
                print("Not Enough Lines")
            else:
                last_n_lines = lines[-n:]
                for line in last_n_lines:
                    print(line.strip())
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An I/O error occurred.")


filename = "example.txt"  # Replace with your filename
n = int(input("Enter the number of lines to read = "))
readLastNLines(filename, n)
