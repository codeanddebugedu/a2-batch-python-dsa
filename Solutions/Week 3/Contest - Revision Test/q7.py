def pattern(rows: int) -> None:
    for i in range(1, rows):
        for j in range(1, i):
            print(" ", end="")
        for k in range(4):
            print("*", end=" ")
        print()


pattern(5)
