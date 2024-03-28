class Student:
    """Create an object of Student with various attributes and features"""

    def __init__(
        self, roll_no: int, name: str, gender: str, age: int, phone_number: int
    ) -> None:
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"Name = {self.name}, age = {self.age}"

    def __add__(self, object2):
        return self.age + object2.age

    def __len__(self) -> int:
        return self.phone_number

    def __gt__(self, object2) -> bool:
        return self.age > object2.age

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


"""
gt
lt
ge
le
eq
ne
"""


s1 = Student(1, "Anirudh", "Male", 26, 8969696569)
s2 = Student(2, "Vandana", "Female", 88, 9999658569)
# print(s1 + s2)
# print(len(s1))
print(s1 >= s2)
