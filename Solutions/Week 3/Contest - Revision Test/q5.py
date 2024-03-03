def pattern(rows: int) -> None:
    for i in range(rows, -1, -1):
        for k in range(rows - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()


pattern(5)
