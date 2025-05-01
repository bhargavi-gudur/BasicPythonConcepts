# This code defines a class named `Student` with 
# a class variable `student` and instance variables for name, age, and grade.
class Student:
    student = "student details"
    def __init__(self, name, age, grade):
        self.n = name
        self.a = age
        self.g = grade

    def display_details(self):
        return f"{Student.student} -> Name: {self.n}, Age: {self.a}, Grade: {self.g}"


# Create instances of the class
student1 = Student("Gandla", 15, "10th")
student2 = Student("Priya", 16, "12th")

# Display student details
print(student1.display_details())
print(student2.display_details())
