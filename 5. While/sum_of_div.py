def sumOfDiv(n1: int, n2: int) -> int:
    i = 1
    total = 0
    while i <= n1:
        if i % n2 == 0:
            total = total + i
        i += 1
    return total


print(sumOfDiv(100, 1))
