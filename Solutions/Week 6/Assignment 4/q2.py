def numbersOddEven(input_file: str, output_file: str):
    try:
        with open(input_file, "r") as file_in:
            with open(output_file, "w") as file_out:
                for line in file_in:
                    number = int(line.strip())
                    if number % 2 == 0:
                        file_out.write(f"{number} Even\n")
                    else:
                        file_out.write(f"{number} Odd\n")
        print(f"Content written to '{output_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except IOError:
        print("Error: An I/O error occurred.")


numbersOddEven("numbers.txt", "numbers_result.txt")
