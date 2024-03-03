def hourglass_pattern(size):
    # Upper half of the hourglass
    for i in range(size, 0, -1):
        for j in range(size - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()

    # Lower half of the hourglass
    for i in range(2, size + 1):
        for j in range(size - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()


hourglass_pattern(5)
