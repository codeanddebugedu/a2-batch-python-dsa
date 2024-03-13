# def add(a, b):
#     # ...
#     return a + b
# 15 -> List[int] [1,2,3,4,,,14,15]

add = lambda a, b: a + b
mul = lambda a, b, c: a * b * c if a != 0 and b != 0 and c != 0 else "Invalid"
make_list = lambda num: [i for i in range(1, num + 1)]

print(add(1, 5))
print(mul(4, 5, 0))

x = make_list(20)
print(x)
