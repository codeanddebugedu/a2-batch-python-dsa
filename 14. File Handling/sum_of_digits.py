# f = open("hello.txt", "r")
# numbers = f.readlines()
# total = 0
# for number in numbers:
#     number = number.strip()
#     total = total + int(number)

# print(total)
# f.close()

f = open("hello.txt", "r")
data = f.read().split()
total = 0
for i in data:
    total = total + int(i)
print(total)
f.close()
