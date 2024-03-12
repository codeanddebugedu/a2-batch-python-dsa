my_dict = {
    "anirudh": 78,
    "akul": 11,
    "muskan": 11,
    "sanjay": None,
}

keyname = input("Enter key name = ")

if keyname in my_dict:
    print(my_dict[keyname])
else:
    print("Key does not exists")

# x = my_dict.get(keyname)
# if x is not None:
#     print(x)
# else:
#     print("Key does not exists")
