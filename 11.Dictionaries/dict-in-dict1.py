students = {
    "anirudh": {"age": 66, "gender": "Male"},
    "sanjay": {"gender": "Male", "age": 32},
    "vandana": {"age": 53, "gender": "Female"},
}

# print(students.items())

x = dict(sorted(students.items(), key=lambda x: x[1]["age"]))
print(x)
# print(x)
