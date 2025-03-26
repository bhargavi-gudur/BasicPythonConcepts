'''
## Dictonary is a collection of key value pairs
## Nested Dictonary is a dictonary inside a dictonary.
## Nested Dictonary is a dictonary inside a dictonary.'''

nested_dict = {"key1": {"rohit", "bhargavi"}, "key2": {123, "bhargavi"}}
print(nested_dict)
print("------------------------------------------------")
student_data = {
    "shiva": {"rollno": 1, "age": 3000, "course": "creation_destory"},
    "ram": {"rollno": 4, "age": 2000, "course": "python "},
    "sita": {"rollno": 5, "age": 2000, "course": "java "},
}
print("------------------------------------------------")
print("ram:", student_data["ram"])
print("student : ", student_data)
print("pop out :", student_data["shiva"].pop("course"), "\n", student_data["shiva"])
print("------------------------------------------------")
for i in student_data:
    print("student_data-> \n key : ", i, "\n value : ", student_data[i])
print("------------------------------------------------")
for i in student_data:
    print("student_data-> \n key : ", i, "\n value : ", student_data[i].items())
print("------------------------------------------------")
for i in student_data:
    print("student_data-> \n key : ",
          student_data[i].keys(), "\n value : ", student_data[i].values())
print("------------------------------------------------")
