try:
    f = open("xyz.txt", "r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("File does not exists")
except:
    print("Some error occurred")
