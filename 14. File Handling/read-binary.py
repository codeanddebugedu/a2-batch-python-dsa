with open("1.pdf", "rb") as f:
    data = f.readlines()

with open("1.pdf", "ab") as f:
    data = data[:-1] + data[:-1] + data[-1:]
    f.writelines(data)
