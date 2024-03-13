students = {
    "sanjay": {"gender": "Male", "age": 32, "marks": [54, 76, 12, 232, 11, 65]},
    "vandana": {"age": 53, "gender": "Female", "marks": [65, 77, 33]},
    "anirudh": {"age": 66, "gender": "Male", "marks": [2, 3, 11, 24, 55]},
}
# print(students.items())
print(dict(sorted(students.items(), key=lambda x: sum(x[1]["marks"]))))
