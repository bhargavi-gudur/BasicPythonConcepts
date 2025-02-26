# Write a program to swap two numbers using function.
  
var_num1 = int(input("enter the value 1: \n"))
var_num2 = int(input("enter the value 2: \n")) 
# method 1
def swap_number(a, b):
    print("before swapping -> ", " a :", a, " b: ", b)
    swap_var = a+b
    print("the sum of swap variable :", swap_var)
    a = swap_var-a
    b = swap_var-b
    print("after swapping -> ", " a :", a, " b: ", b)
# method 2
def swap_twoVar(a, b):
    print("before swapping -> ", " a :", a, " b: ", b)
    a = a+b
    b = a-b
    a = a-b
    print("after swapping -> ", " a :", a, " b: ", b)

print(" method 1  swap two numbers using three variable") 
swap_number(var_num1, var_num2)
print(" method 2 swap two numbers using two variable")
swap_twoVar(var_num1, var_num2)