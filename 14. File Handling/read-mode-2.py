# Read mode

f = open("hello.txt", "r")

d = f.readlines()
print(d[2])

# d = f.readline()
# print(d)


# d = f.read(15)
# print(d)
# d = f.read(5)
# print(d)
# d = f.read()
# print(d)
# d = f.read()
# print(d)

f.close()
