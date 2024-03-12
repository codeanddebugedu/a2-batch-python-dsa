"""
Store name as a Key, and 5 marks in a List as a value in dictionary. 
Store details of at least 5 students. 
Print only the total marks of every student in ascending order.
"""

students = {
    "Anirudh": [12, 43, 1, 76, 23],
    "Akul": [78, 82, 80, 43, 62],
    "Nihar": [13, 72, 32, 89, 53],
    "Anusha": [43, 12, 79, 82, 85],
    "Muskan": [54, 87, 72, 86, 84],
}


all_total_marks = []
for marks in students.values():
    total_marks = sum(marks)
    all_total_marks.append(total_marks)

all_total_marks.sort()

print(all_total_marks)
