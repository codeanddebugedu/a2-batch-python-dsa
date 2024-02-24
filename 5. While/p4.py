# 1 11 101 1001 10001 100001 1000001


def pattern(n):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = (10**i) + 1
        i += 1
    print()


pattern(10)
pattern(5)
