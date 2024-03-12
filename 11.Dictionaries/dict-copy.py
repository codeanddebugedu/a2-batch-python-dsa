import copy

my_dict = {
    "anirudh": 78,
    "akul": [4, 5, 33, 11],
    "muskan": 11,
}

a = copy.deepcopy(my_dict)
a["akul"].append(100)

print(my_dict)
print(a)

# print(id(my_dict["akul"]))
# print(id(a["akul"]))

# a["xyz"] = 100

# print(my_dict)
# print(a)

# new_dict = my_dict.copy()
