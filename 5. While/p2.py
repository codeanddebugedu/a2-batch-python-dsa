# 1 2 4 8 16 32 64...upto N times


def pattern(n: int):
    i = 1
    number = 1
    while i <= n:
        print(number, end=" ")
        number = number * 2
        i += 1


pattern(10)
