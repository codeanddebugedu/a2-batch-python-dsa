with open("hello.txt", "r") as f:
    data = f.read(5)
    print(data)
    data = f.read(5)
    print(data)

data = f.read()
print("Done")
