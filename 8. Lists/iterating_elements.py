# Iterating/Iteration
a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765]


# i = 0
# while i < len(a):
#     print(a[i], end=" ")
#     i += 1

# Traverse by index
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# Reverse
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")
# for i in range(-1, -(len(a) + 1), -1):
#     print(a[i], end=" ")
