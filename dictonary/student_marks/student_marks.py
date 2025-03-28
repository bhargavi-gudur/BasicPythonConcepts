student_marks = {"bhargavi": 96,
                 "jenny": 92,
                 "keerthi": 89,
                 "rani": 74,
                 "priyadeepa": 56,
                 "aruna": 12
                 }
student_grade = {}

for student in student_marks:
    print("key:", student)
    print("values", student_marks[student])

    marks = student_marks[student]
    if marks > 90:
        student_grade[student] = "A+"
    elif marks > 80:
        student_grade[student] = "A"
    elif marks > 70:
        student_grade[student] = "b+"
    elif marks > 50:
        student_grade[student] = "c"
    else:
        student_grade[student] = "F"
print("grades:", student_grade)
