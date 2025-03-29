# stringMethod/string_typeCon.py
# example of string type conversion
# string to int conversion
import sys
sys.path.append('../../log_art')
from log_art import log_art
print(log_art.log_type_casting)

# Removed log import and related code as it is not required
def typecasting(typeofvariable):
    var = 0
    for i in range(len(typeofvariable)):
        var = var + int(typeofvariable[i])
        print(f"{i} sum of the var:{var}")
    print(f" final sum :{var}")
    print(f"var -> {type(var)}\ntypeofvariable ->{type(typeofvariable)}")

# this is a string type conversion example
def string_type_conversion():
    print("String type conversion started.")
    continue_flag = input(
        "Do you want to continue? (yes/no): ").strip().lower()
    while continue_flag != "NO":
        typeofvariable = input(" enter the value  to convert data conversion?")
        typecasting(typeofvariable)
        continue_flag = input("Do you want to continue? (yes/no): ").strip().lower()
    print("Goodbye!")
        
string_type_conversion()
