f = open("hello.txt", "r")

for line in f:
    print(len(line.split()))

# lines = f.readlines()

# for line in lines:
#     print(len(line.split()))
# print(len(line.strip()))

f.close()
