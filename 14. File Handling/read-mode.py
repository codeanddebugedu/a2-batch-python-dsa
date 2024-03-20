# Read mode

f = open("hello.txt", "r")
data = f.read()  # Reads whole file

for i in data:
    print(i)

# for line in f:
#     print(line, end="")


f.close()
