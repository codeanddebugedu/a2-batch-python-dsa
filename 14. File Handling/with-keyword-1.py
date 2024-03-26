# with open("hello.txt", "r") as f1:
#     data = f1.read()

# with open("hello1.txt", "w") as f2:
#     f2.write(data)

with open("hello.txt", "r") as f1, open("hello1.txt", "w") as f2:
    f2.write(f1.read())
