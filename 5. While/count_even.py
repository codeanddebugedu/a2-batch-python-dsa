# 1 to 100,,,how many even numbers there?

i = 1
count = 0
while i <= 100:
    if i % 2 == 0 or i % 3 == 0:
        print(i, end=" ")
        count = count + 1
    i += 1
print()
print(count)
