class Student:
    def __init__(self):
        self.name = input("Enter student's name: ")
        self.age = int(input("Enter student's age: "))
        self.gender = input("Enter student's gender (Male/Female/Other): ")
        self.marks = []
        print("Enter 5 marks:")
        for _ in range(5):
            mark = int(input())
            self.marks.append(mark)

    def displayAllInfo(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Marks: {self.marks}")

    def displayOnlyMarks(self):
        print(f"Marks: {self.marks}")

    def getTotal(self):
        return sum(self.marks)

    def getMax(self):
        return max(self.marks)

    def getMin(self):
        return min(self.marks)

    def getAvg(self):
        return sum(self.marks) / len(self.marks)

    def addMark(self, mark):
        self.marks.append(mark)

    def removeMark(self):
        if self.marks:
            self.marks.pop()
        else:
            print("No marks to remove.")


if __name__ == "__main__":
    student1 = Student()

    student1.displayAllInfo()
    print(f"Total Marks: {student1.getTotal()}")
    print(f"Max Marks: {student1.getMax()}")
    print(f"Min Marks: {student1.getMin()}")
    print(f"Average Marks: {student1.getAvg()}")

    student1.addMark(95)
    print(f"Updated Marks after adding a new mark: {student1.marks}")

    student1.removeMark()
    print(f"Updated Marks after removing the last mark: {student1.marks}")
