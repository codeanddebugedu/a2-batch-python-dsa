student_data = {
    "Alice": [85, 90, 88, 92, 89],
    "Bob": [78, 82, 79, 81, 80],
    "Charlie": [92, 95, 88, 85, 91],
    "Diana": [76, 80, 79, 82, 85],
    "Eva": [88, 92, 85, 90, 87],
    "Frank": [83, 85, 80, 86, 88],
    "Gina": [90, 87, 92, 88, 86],
}


sorted_student_data = dict(sorted(student_data.items(), key=lambda x: sum(x[1])))

for name, marks in sorted_student_data.items():
    total_marks = sum(marks)
    print(f"{name} has scored {total_marks}")
