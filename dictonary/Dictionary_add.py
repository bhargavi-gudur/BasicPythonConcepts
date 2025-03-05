new_student = {}
student_data = [
    {
        "name": "shiva",
        "rollno": 1,
        "age": 30,
        "course": "c"
    },
    {
        "name": "ram",
        "rollno": 4,
        "age": 26,
        "course": "python "
    },
    {
        "name": "sita",
        "rollno": 5,
        "age": 25,
        "course": "java "
    },
]


def add_new_student(name, rollno, age, course):
    new_student = {"name": name, "rollno": rollno,
                   "age": age, "course": course}

    student_data.append(new_student)
    return student_data


print(add_new_student("laxman", 6, 20, "C++"))

for i in student_data:
    print("Name: ", i["name"])
    print("Rollno: ", i["rollno"])
    print("Age: ", i["age"])
    print("Course: ", i["course"])

for i in student_data:
    print(student_data.index(i)+1, i["name"],
          i["rollno"], i["age"], i["course"])
