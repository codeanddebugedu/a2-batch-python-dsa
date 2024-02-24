# 10 20 30 40 50 60


def pattern(n: int):
    i = 1
    num = 10
    while i <= n:
        print(num, end=" ")
        num = num + 10
        i += 1


pattern(10)
