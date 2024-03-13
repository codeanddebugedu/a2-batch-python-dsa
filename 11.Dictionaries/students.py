my_details = [
    {"name": "Anirudh", "age": 67, "gender": "Male"},
    {"name": "Clara", "age": 52, "gender": "Female"},
    {"name": "Vandana", "age": 63, "gender": "Female"},
    {"name": "Amber", "age": 23, "gender": "Male"},
]


def abc(fffff):
    # print(f"-----> {fffff}")
    return fffff["age"]


my_details.sort(key=abc, reverse=True)
print(my_details)

# my_details.sort(key=lambda z: z["age"], reverse=True)
# print(my_details)
