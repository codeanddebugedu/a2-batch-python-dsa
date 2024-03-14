a = [12, 43, 54, 654, 6, 1, 3243, 543]


def change(x):
    if x % 2 == 0:
        return x + 1
    return x - 1


b = list(map(change, a))
print(b)
