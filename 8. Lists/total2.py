a = [78, 67, 44, -100, 87, 33, 31]

# total = 0
# for i in a:
#     if i % 2 == 0:
#         total = total + i

total = 0
for i in range(len(a)):
    if i % 2 == 0:
        total = total + a[i]

print(total)
