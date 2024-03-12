"""
anirudh has scored 432 marks
sagar has scored 412 marks

"""

"""
print average marks of each student 
print total marks of the class
print the max and min marks of every student
print the average marks scored by whole class

print the maximum mark in that class
"""

students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11, 54, 43, 11],
    "akul": [52, 47, 85],
}

for name, marks in students.items():
    total_marks = 0
    for m in marks:
        total_marks += m
    print(f"{name} has scroed {total_marks} marks")
