"""
Store name as a Key, and 5 marks in a List as a value in dictionary. 
Store details of at least 5 students. 
Print the total marks with percentage of each and every student
"""


def calculatePercentage(total_marks):
    return (total_marks / 500) * 100


students = [
    {"name": "Anirudh", "marks": [12, 43, 1, 76, 23]},
    {"name": "Akul", "marks": [78, 82, 80, 43, 62]},
    {"name": "Nihar", "marks": [13, 72, 32, 89, 53]},
    {"name": "Anusha", "marks": [43, 12, 79, 82, 85]},
    {"name": "Muskan", "marks": [54, 87, 72, 86, 84]},
]

for student in students:
    total_marks = sum(student["marks"])
    percentage = calculatePercentage(total_marks)
    print(
        f"Name: {student['name']}, Total Marks: {total_marks}, Percentage: {percentage:.2f}%"
    )
