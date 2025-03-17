# using function a sample python code for variable concept.
# while loop print name based upon number of time loop.
print("--------variable function ---------------")
number = int(input("enter the number :"))
def name_string():
    for i in range(number):
        name = input(" enter your name : ")
        print(f"my name is {name}")
print("-----------------------------------")
name_string()

print("---------swap the int number ------------------")
def swap_num():
    for i in range(number):
        number1 = int(input("enter the number1 :"))
        number2 = int(input("enter the number2 :"))
        print(f"before swapping the numbers {i} -> {number1} , {number2} ")
        number1 = number1+number2
        number2 = number1-number2
        number1 = number1-number2
        print(f"after swapping the numbers {i} -> {number1} , {number2} ")
        print("-----------------------------------")
swap_num()



