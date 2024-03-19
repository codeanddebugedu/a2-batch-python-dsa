"""Q1. Here’s a students data and their marks.
student_data = { 
"Alice": [85, 90, 88, 92, 89],
"Bob": [78, 82, 79, 81, 80],    
"Charlie": [92, 95, 88, 85, 91],  
"Diana": [76, 80, 79, 82, 85],  
"Eva": [88, 92, 85, 90, 87],   
"Frank": [83, 85, 80, 86, 88],   
"Gina": [90, 87, 92, 88, 86],}
Display the name of student and total marks in ascending order.
OUTPUT:
Bob has scored 400
Diana has scored 402
Frank has scored 422
Eva has scored 442
Gina has scored 443
Alice has scored 444
Charlie has scored 451"""

student_data = {
    "Alice": [85, 90, 88, 92, 89],
    "Bob": [78, 82, 79, 81, 80],
    "Charlie": [92, 95, 88, 85, 91],
    "Diana": [76, 80, 79, 82, 85],
    "Eva": [88, 92, 85, 90, 87],
    "Frank": [83, 85, 80, 86, 88],
    "Gina": [90, 87, 92, 88, 86],
}
# print(student_data.items())
details = dict(sorted(student_data.items(), key=lambda x: sum(x[1])))

for k, v in details.items():
    sum = 0
    for i in v:
        sum += i
    print(f"{k} has socred {sum}")
