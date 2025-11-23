"""
@file Attendance.py
@author Gandla Bhargavi 
@brief Marks student attendance (Present/Absent) and displays it with current date.

Input  : Student name + P/A
Output : Attendance record with status and date

@date 2025-11-23
"""

class Attendance:
    def __init__(self):
        self.name = ""
        self.status = ""

    # Taking attendance input
    def input_details(self):
        self.name = input("Enter student name : ")
        self.status = input("Enter attendance (P/A): ")

    # Display attendance result
    def display(self):
        print("\n--- Attendance Record ---")
        print(f"Name     : {self.name}")
        print(f"Status   : {'Present' if self.status.lower() == 'p' else 'Absent'}")
        print("Date     : 23-11-2025")


def main():
    student = Attendance()
    student.input_details()
    student.display()


if __name__ == "__main__":
    main()