# ASCII
my_string = "python is a great language"

count = 0
for char in my_string:
    ascii_number = ord(char)
    if ascii_number == 101 or ascii_number == 69:
        count += 1
print(count)

# count = 0
# for char in my_string:
#     if char == "e" or char == "E":
#         count += 1
# print(count)
