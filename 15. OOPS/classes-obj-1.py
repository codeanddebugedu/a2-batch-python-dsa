class Student:
    """Create an object of Student with various attributes and features"""

    def __init__(self) -> None:
        self.roll_no = int(input("Enter roll no = "))
        self.name = input("Enter name = ")
        self.gender = input("Enter gender = ")
        self.age = int(input("Enter age = "))
        self.phone_number = int(input("Enter phone = "))

    def updateName(self) -> None:
        self.name = input("Enter new name = ")

    def updatePhoneNumber(self, new_number=0) -> None:
        self.phone_number = new_number

    def display(self) -> None:
        """Display all the info related to a Student"""
        print(f"Roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")
        print(f"Phone number = {self.phone_number}")


s1 = Student()
print(s1.display.__doc__)
