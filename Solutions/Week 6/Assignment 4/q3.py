def multiplication(filename: str, number: int) -> None:
    try:
        with open(filename, "w") as file:
            for i in range(1, 11):
                result = number * i
                file.write(f"{number} x {i} = {result}\n")
        print(
            f"Multiplication table of {number} is written to '{filename}' successfully."
        )
    except IOError:
        print("Error: An I/O error occurred.")


multiplication("multiplication_table.txt", 5)
