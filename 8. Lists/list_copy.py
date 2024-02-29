import copy

a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]

b = copy.copy(a)  # Shallow Copy
b = copy.deepcopy(a)  # Deep Copy

print("A ->", a, id(a))
print("B ->", b, id(b))

b[3][1] = 1000

print("A ->", a, id(a))
print("B ->", b, id(b))
