class Student:
    def __init__(self, name, roll_number, total_marks):
        self.name = name
        self.roll_number = roll_number
        self.total_marks = total_marks

name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
total_marks = int(input("Enter total marks: "))

student = Student(name, roll_number, total_marks)

print()
print("Student Details")
print("Name:", student.name)
print("Roll Number:", student.roll_number)
print("Total Marks:", student.total_marks)
