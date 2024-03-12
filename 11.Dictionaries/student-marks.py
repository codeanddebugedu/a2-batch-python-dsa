"""
Q1
anirudh has scored 432 marks
sanjay has scored 112 marks

Q2
anirudh has scored 87.44%
sanjay has scored 55.22%
"""

students = {
    "anirudh": {"physics": 54, "maths": 11, "english": 99, "history": 43},
    "sanjay": {"physics": 13, "maths": 40},
    "vandana": {"physics": 65, "maths": 85, "english": 94},
}

for name, marks in students.items():
    total_marks = 0
    for m in marks.values():
        total_marks += m
    print(f"{name} has scored {total_marks} marks")
    print(f"{name} has scored {total_marks/len(marks):.2f}%")
