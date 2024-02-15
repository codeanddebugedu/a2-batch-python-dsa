score: int = int(input("Enter the student's score: "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
elif score >= 1 and score < 60:
    print("F")
else:
    print("Invalid")
